Curso de Flask
---

# Fundamentos de Flask

Flask es sencillo de aprender, tiene una documentación clara y práctica, es rápido a la hora de renderizar puede ser hasta tres veces más rapido que Django. También es fácil de realizar una API REST, la estructura de un proyecto es flexible y es ideal para aprender desarrollo web con un framework de Python.

## ¿Cómo funcionan las aplicaciones de internet?

Cuando utilizas una aplicación web puedes interactuar con ella desde una computadora hasta un dispositivo móvil, pero esto no quiere decir que consume el procesamiento de tu dispositivo. Todo lo contrario, se hace en una red de servidores.

Estos servidores unen su poder de procesamiento con el fin transmitir solicitudes a todo el mundo, a su vez utilizar servidores especializados para almacenar los datos con los cuales se está trabajando, así como los datos de los demás usuarios. Como todo esto sucede sin demora alguna, parecerá que la aplicación se está ejecutando de forma nativa en tu dispositivo.

El servidor procesa la información obtenida por el navegador, luego se realizan los procedimientos necesarios de acuerdo a la lógica de negocio de la aplicación para regresar la información solicitada al cliente.

**Ejemplo:**

Cuando utilizamos Google Drive el cual es una aplicación web y abrimos un documento con Google Docs, el navegador se comunica con los servidores para ver y editar el documento.

A medida que vayas editando el documento, tu navegador trabajará de la mano con los servidores para asegurarse que todos los cambios se estén guardando.

**Ventajas:**

* Muchas de las aplicaciones web que existen son gratuitas.
* Puedes acceder a tu información en cualquier momento y lugar.
* No dependes de un dispositivo en específico ya que la aplicación se encuentra almacenada en la web.

## ¿Qué es Flask?

Flask es un framework minimalista escrito en Python que permite crear aplicaciones web rápidamente y con un mínimo de líneas de código, busca que su infraestructura inicial sea lo más simple posible y pueda personalizarse fácilmente, puedes extender sus funcionalidades con las llamadas Flask Extensions http://flask.pocoo.org/extensions/

Se diferencia de Django porque este tiene una estructura más compleja donde todo lo necesario ya viene incluido incluso aunque en ciertos casos no se necesiten todas las características del framework.

Flask usa un sistema de plantillas llamado Jinja2 que está basado en el sistema de Django Templates

## Instalación de Python, pip y virtualenv

Esta es la guía para configurar nuestro ambiente con Python 3.
Por lo general Mac ya incluye una instalación de Python, la puedes verificar ejecutando los siguientes comandos en una terminal:
```
python --version
python3 --version
```

Debemos asegurarnos de tener python 3. Para instalar Python puedes seguir el siguiente enlace y después regresar a esta lectura.

https://platzi.com/clases/1378-python/14289-guia-de-instalacion-y-conceptos-basicos/

Instalación en Windows
Una vez que instalaste python 3 desde python.org vamos a verificar que también incluimos pip en esta instalación. Después debes correr el siguiente comando para instalar virtualenv:
```
pip install virtualenv
```

El sistema debe haber instalado virtualenv y ahora podemos comenzar con el curso.

Instalación en Mac
Si ya instalaste python 3 ahora corre el siguiente comando para instalar pip:
```
sudo easy_install pip
```
Para install virtualenv de manera global corre:
```
pip install virtualenv
```
El sistema debe haber instalado virtualenv y ahora podemos comenzar con el curso.

## Hello World Flask

Estos son los conceptos principales que debes entender antes de hacer un Hello World en Flask:

* virtualenv: es una herramienta para crear entornos aislados de Python.

* pip: es el instalador de paquetes para Python.

* requirements.txt: es el archivo en donde se colocará todas las dependencias a instalar en nuestra aplicación.

* FLASK_APP: es la variable para identificar el archivo donde se encuentra la aplicación.

Entonces:

* Creamos un ambiente virtual `python -m venv venv`
* Lo activamos `source venv/bin/activate`
* Instalamos flask con pip `pip install flask`
* Creamos archivo que guarda las dependencias a instalar `pip freeze > requeriments.txt`

Ahora ya podemos trabajar en nuestro script. En este:
* Importamos la clase Flask `from flask import Flask`. Esta nos va a permitir crear nuevas instancias de Flask.
* Creamos una nueva instancia y la guardamos en la variable `app`, llamando Flask con el nombre de la apliación `app = Flask(__name__)`

* Ahora se crea una función que va regresar el hello world y se desplegará ligandola con flask, esto se hace con el decorador `@app.route`, esta recibe como parámetro la ruta donde se va a correr la función. 
```
@app.route('/')
def hello():
    return 'Hello World Flask'
```

* Para activar un servidor y correr la aplicación podemos ejecutar el comando `flask run`. No sin antes declarar la variable `FLASK_APP` así `export FLASK_APP=main.py`
