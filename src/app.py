from flask import Flask, render_template
import os
import sqlite3

app = Flask(__name__)
def crear_conexion(path_database):
    try:
        conexion=sqlite3.connect(path_database)
        cursor=conexion.cursor()
    except:
        print("Error al conectar con la base de datos")
    return conexion, cursor

def crear_tabla_usuarios(conexion, cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            dni TEXT,
            fecha_nacimiento TEXT,
            direccion TEXT,
            correo_electronico TEXT
    );         
    ''')
    conexion.commit()

def anadir_usuarios(conexion, cursor):
    cursor.executemany("insert into usuarios values (?,?,?,?,?,?);",
        [
            (None,'Loreto','36581601D','04-05-1998','Calle Gutierrez mellado, 13','Loreto@gmail.com'),
            (None,'Carlos','56396587N','05-11-1980','Calle princesa, 6','Carlos@gmail.com'),
            (None,'Pablo','25649656X','10-09-1990','Avenida del mar, 12','Pablo@gmail.com'),
            (None,'David','65365246M','05-06-2000','Calle Fiesta, 2','David@gmail.com'),
            (None,'Sergio','25469632F','01-08-2005','Calle reina Sofía, 4','Sergio@gmail.com'),
            (None,'Angel','45635423L','14-11-1983','Calle de los apóstoles, 54','Angel@gmail.com'),

        ])
    conexion.commit()
def dame_usuarios(cursor):
    cursor.execute("select * from usuarios")
    tuplas=cursor.fetchall()
    if len(tuplas)==0:
        return None
    else:
        return tuplas
@app.route("/")
@app.route("/index")
def index():
    path_database="avanza.db"
    inicializar_bd=False
    if not os.path.exists(path_database):
        inicializar_bd=True
    conexion, cursor=crear_conexion(path_database)
    # Se crea la tabla y los archivos si el archivo veterinario-Avanza-Plus.db no existe
    if inicializar_bd:
        crear_tabla_usuarios(conexion, cursor)
        anadir_usuarios(conexion, cursor)
    #usuarios=["Fran", "Kike", "Pablo","Teo"]
    usuarios=dame_usuarios(cursor)
    print(usuarios)
    return render_template("index.html", usuarios=usuarios)


# Start the Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)