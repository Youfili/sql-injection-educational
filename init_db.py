'''
Script che inizializza il DB
'''
import sqlite3


with open('schema.sql', 'r') as f:
    schema = f.read()
    # tutte le righe del codice SQL vengono lette 'read' e lo script viene eseguito da connection

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.executescript(schema)    # --> uso executescript per più query
connection.commit()
connection.close()

