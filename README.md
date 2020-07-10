# Patli:
Sistema de control de expedientes, y pacientes medicos para poder llevar un siguimiento, el cual al llenar los datos requeridos te genera una receta medica

## Contenido:
El proyecot solo tiene una rama: **master** es la unica rama existente.

## Demomostracion:
Por el momento no tiene un sitio para hacer la demostración pero se subira a heroku.

## Para bajar el repositorio
Se necesitan estos requerimientos especiales para poder bajar el repositorio, seguirlos en el orden marcado si no fallara su ejecución:
* Primer paso:
    * Instalar MySQL o MariaDB
* Segundo paso: 
    * Instalar la versión de python más reciente
* Tercer paso:
    * Instalar pip en caso de no instalarse junto con python
* Cuarto paso:
    * Instalar paqueterias Flask, enum, docx, Flask-Login, Flask-SQLAlchemy, Flask-WTF, Jinja2, python-docx, Werkzeug, WTForms
* Quinto paso crear base de datos:
    * crear la base de datos pythonp

## Instalación:
Para instalar y correr el proyecto se agregan instrucciones para poder hacer que se ejecute el mismo:
```Terminal Linux
yum -y install mariadb 
```Terminal MacOS
brew install mysql
```Terminal
mysql create database pythonp;
```Terminal
pip3 install Flask enum docx Flask-Login Flask-SQLAlchemy Flask-WTF Jinja2 python-docx Werkzeug WTForms
```Terminal 
python3 run.py
```
### Notas
Una vez instalado y corriendo el software podras verlo en cualquier navegador entrando a 127.0.0.1/login, **instalar todas las dependencias ya que si no podra ejecutarse el programa**