"""
Ejercicio1: Base de Datos Administradas vs No Administradas

Entender la diferencia entre bases de datos administradas y no administradas
"""
import sqlite3
import time

# Simulación de base de datos no administrada

# Conexión a la base de datos no administrada llamada 'unmanaged.db'
conn = sqlite3.connect('unmanaged.db')
cursor = conn.cursor()

# Creación de la tabla 'users' si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')

# Inserción de un registro en la tabla 'users'
cursor.execute('''INSERT INTO users (name) VALUES ('Alice')''')

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

# Simulación de base de datos administrada

class ManagedDatabase:
    def __init__(self, db_name):
        # Inicialización y conexión a la base de datos administrada
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_backup()
    
    def execute_query(self, query):
        # Ejecuta una consulta y crea una copia de seguridad después de cada ejecución
        self.cursor.execute(query)
        self.conn.commit()
        self.create_backup()
    
    def create_backup(self):
        # Crea una copia de seguridad de la base de datos
        with open('backup.sql', 'w') as f:
            for line in self.conn.iterdump():
                f.write('%s\n' % line)
        print("Backup created at", time.ctime())

# Creación de una instancia de la base de datos administrada
managed_db = ManagedDatabase('managed.db')

# Creación de la tabla 'users' si no existe en la base de datos administrada
managed_db.execute_query('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')

# Inserción de un registro en la tabla 'users'
managed_db.execute_query('''INSERT INTO users (name) VALUES ('ZZ')''')
