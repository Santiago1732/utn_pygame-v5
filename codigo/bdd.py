import sqlite3

def crear_db():
    try:
        conexion = sqlite3.connect("../base_de_datos/database.db")
        cursor = conexion.cursor()
        # Crear una única tabla jugador con dos columnas: nombre y lv
        cursor.execute("CREATE TABLE jugador (nombre VARCHAR(50), lv VARCHAR(50), tiempo_total VARCHAR(50))")
        conexion.commit()
    except Exception as ex:
        print(ex)
    finally:
        if conexion:
            conexion.close()

def insertar_jugador(nombre_jugador, current_level_index,tiempo_total):
    try:
        conexion = sqlite3.connect("../base_de_datos/database.db")
        cursor = conexion.cursor()

        # Insertar datos
        cursor.execute("INSERT INTO jugador (nombre, lv, tiempo_total) VALUES (?, ?, ?)", (nombre_jugador, current_level_index,tiempo_total))

        # Guardar los cambios
        conexion.commit()
    except Exception as ex:
        print(ex)
    finally:
        # Cerrar la conexión
        if conexion:
            conexion.close()





