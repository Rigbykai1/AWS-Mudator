import requests
import subprocess


def verificar_o_crear_repositorio_github(nombre_repositorio, nombre_usuario, token):
    url_creacion = "https://api.github.com/user/repos"  # Cambiado a la URL de la API
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Crear el repositorio en GitHub
    datos_repositorio = {
        "name": nombre_repositorio,
        "private": True  # Cambia a False si deseas que el repositorio sea público
    }
    respuesta_creacion = requests.post(
        url_creacion, json=datos_repositorio, headers=headers)

    if respuesta_creacion.status_code == 201:
        print(f"El repositorio '{
              nombre_repositorio}' ha sido creado exitosamente en GitHub.")
        # URL del nuevo repositorio
        return f"https://github.com/{nombre_usuario}/{nombre_repositorio}"
    else:
        print(f"Error al crear el repositorio '{
              nombre_repositorio}': {respuesta_creacion.text}")
        return None


def verificar_o_crear_repositorio_gitlab(nombre_repositorio, token, grupo_id):
    url_creacion = "https://gitlab.com/api/v4/projects"
    headers = {
        'Private-Token': token,
        'Content-Type': 'application/json'
    }

    # Crear el repositorio en GitLab
    datos_repositorio = {
        "name": nombre_repositorio,
        "namespace_id": grupo_id,  # ID del grupo donde se creará el repositorio
        "visibility": "private"  # Cambia a "public" si deseas que el repositorio sea público
    }
    respuesta_creacion = requests.post(
        url_creacion, json=datos_repositorio, headers=headers)

    if respuesta_creacion.status_code == 201:
        print(f"El repositorio '{
              nombre_repositorio}' ha sido creado exitosamente en GitLab.")
        # URL del nuevo repositorio
        return f"https://gitlab.com/{grupo_id}/{nombre_repositorio}"
    else:
        print(f"Error al crear el repositorio '{
              nombre_repositorio}': {respuesta_creacion.text}")
        return None


def migrar_repositorios(archivo_repositorios, nombre_usuario, token, proveedor, grupo_id=None):
    with open(archivo_repositorios, 'r') as file_repos:
        repositorios = file_repos.readlines()

    for repo_url in repositorios:
        repo_url = repo_url.strip()
        if not repo_url:
            continue

        # Extraer el nombre del repositorio a partir de la URL
        nombre_repositorio = repo_url.split('/')[-1].replace('.git', '')

        # Crear el repositorio en el proveedor elegido
        if proveedor.lower() == 'github':
            destino_url = verificar_o_crear_repositorio_github(
                nombre_repositorio, nombre_usuario, token)
        elif proveedor.lower() == 'gitlab':
            destino_url = verificar_o_crear_repositorio_gitlab(
                nombre_repositorio, token, grupo_id)
        else:
            print(f"Proveedor desconocido: {
                  proveedor}. Debe ser 'github' o 'gitlab'.")
            continue

        if destino_url is None:
            print(f"No se pudo crear el repositorio '{nombre_repositorio}'.")
            continue

        print(f"Clonando repositorio: {nombre_repositorio}")
        # Clonar el repositorio desde AWS CodeCommit
        subprocess.run(['git', 'clone', '--mirror',
                       repo_url, nombre_repositorio])

        print(f"Configurando nuevo remoto para: {nombre_repositorio}")
        # Configurar el nuevo remoto
        subprocess.run(['git', 'remote', 'add', 'destino', destino_url])

        print(f"Empujando {nombre_repositorio} al nuevo remoto: {destino_url}")
        # Empujar el repositorio al nuevo remoto
        subprocess.run(['git', 'push', 'destino', '--mirror'])

        print(f"Migración completada para: {nombre_repositorio}\n")


# Ejecución del script
# Archivo con las URLs de los repositorios de AWS CodeCommit
archivo_repositorios = 'repositorios.txt'
token = "your_token_here"  # Token de acceso personal (GitHub o GitLab)

# Elegir proveedor
proveedor = input("Ingrese el proveedor (github/gitlab): ").strip().lower()
grupo_id = None
if proveedor == 'gitlab':
    grupo_id = input(
        "Ingrese el ID del grupo donde se creará el repositorio en GitLab: ")
nombre_usuario = input("Ingrese su nombre de usuario de GitHub: ")

migrar_repositorios(archivo_repositorios, nombre_usuario,
                    token, proveedor, grupo_id)
