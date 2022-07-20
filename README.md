# SQLImporter
Simple tool to import all SQL files in a folder, including subfolders.

### How to use
Tienes que poner el archivo .exe o .py y databaseAuth.json en la carpeta raiz del servidor, después tienes que editar databaseAuth.json con los datos de la base de datos, cuando lo ejecutas se importan todos los archivos que encuentran en la carpeta del servidor, también incluye subcarpetas, ejemplo: C:\Users\YourUsername\Desktop\FivemServer\resources\esx\es_extended\es_extended.sql

### Important
The program will import all the files it finds, if there is a file that is already uploaded to the sql it will give an error, but it will continue importing the files to the database, it is recommended to delete the entire database and let the program amount from 0.
