# Migración de Repositorios

_Este proyecto permite migrar repositorios desde AWS CodeCommit a GitHub o GitLab de manera sencilla y automatizada. Actualmente está en fase beta, por lo que se agradecen todos los aportes y sugerencias._

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Para utilizar el código, debes tener instalado Git y clonar el repositorio en la carpeta que deseas. Abre un terminal y ejecuta el siguiente comando:

```
git clone https://github.com/tu_usuario/migracion-repositorios.git
```

### Instalación 🔧

1. Asegúrate de tener Python y Git instalados en tu máquina.
2. Instala las dependencias necesarias ejecutando el siguiente comando:

```bash
pip install requests
```

3. Crea un archivo de texto llamado `repositorios.txt` en el mismo directorio que el script, y coloca las URLs de los repositorios de AWS CodeCommit que deseas migrar, cada uno en una línea.

## Uso 👌

1. Abre el archivo del script en tu editor de texto preferido.
2. Asegúrate de reemplazar `Tutoken` con tu token de acceso personal de GitHub o GitLab.
3. Ejecuta el script con Python:

```bash
python migracion_repositorios.py
```

4. Cuando se te solicite, ingresa el proveedor (`github/gitlab`) y, si es necesario, el ID del grupo de GitLab.

## Construido con 🛠️

* [Python](https://www.python.org/) - Lenguaje de programación utilizado
* [Requests](https://docs.python-requests.org/en/master/) - Librería para realizar solicitudes HTTP

## Contribuyendo 🖇️

Para contribuir, realiza un fork del repositorio, crea una nueva rama, realiza tus cambios y envía un pull request especificando en el commit lo que realizaste y el propósito de ello. Todos los aportes son bienvenidos, especialmente durante esta fase beta.

## Versionado 📌

Para el versionado, utilicé git, por lo que puedes ver los cambios realizados desde que publiqué el primer código.

## Autores ✒️

* **Rigbykai1** - *Migración de Repositorios* - [Tu GitHub](https://github.com/rigbykai1)

## Licencia 📄

Aún sin licencia, pero puedes usarlo libremente y aportar mejoras si así lo deseas.

## Muchas gracias por leerme hasta acá 🥳

* Comenta a otros sobre este proyecto 📢
* Da las gracias públicamente 🤓.

## Menciones

Plantilla realizada con ❤️ por [Villanuevand](https://github.com/Villanuevand) 😊

### Personaliza el `README.md`
Recuerda reemplazar `tu_usuario` y `Tu Nombre` por tu información real y cualquier otro detalle que desees añadir. Este documento informará a los usuarios sobre la fase beta y los animará a contribuir al proyecto.
