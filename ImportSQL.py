from pathlib import Path
import mysql.connector
import json
import os 
import time

print("Made by: https://github.com/DaniiGP")
time.sleep(0.5)
print("Make sure to change the data in the file: databaseAuth.json")
time.sleep(3)

dir_path = os.path.dirname(os.path.realpath(__file__))

f = open(f'{dir_path}/databaseAuth.json')
  
data = json.load(f)

path = Path(rf'{dir_path}')

cnx = mysql.connector.connect(
    host=data['databaseHost'],
    user=data['databaseUser'],
    password=data['databasePassword'],
    database=data['databaseName']
)
cursor =cnx.cursor()

def executeScriptsFromFile(filename):
    fd = open(filename, 'r')
    sqlFile = fd.read()
    a = sqlFile.replace("CREATE DATABASE IF NOT EXISTS `es_extended`", f"CREATE DATABASE IF NOT EXISTS `{data['databaseName']}`")
    b = a.replace("CREATE DATABASE IF NOT EXISTS `essentialmode`", f"CREATE DATABASE IF NOT EXISTS `{data['databaseName']}`")
    c = b.replace("USE `es_extended`;", f"CREATE DATABASE IF NOT EXISTS `{data['databaseName']}`")
    d = c.replace("USE `essentialmode`;", f"USE `{data['databaseName']}`;")
    fd.close()
    sqlCommands = d.split(';')

    for command in sqlCommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except:
            pass

for o in path.rglob('*.sql'):
    if o.is_file():
        text = o.read_text()
        print(f"Reading File: {o}")

        executeScriptsFromFile(o)
        cnx.commit()
        
        print(f"SQL Inserted: {o}")
        time.sleep(10)

f.close()

print("All SQL files have already been entered into the database")