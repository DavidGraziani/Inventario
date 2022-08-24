import sqlite3
NOMBRE_BASE_DE_DATOS = "inventario.db"

def obtener_conexion():
    return sqlite3.connect(NOMBRE_BASE_DE_DATOS)

def crear_tablas():
    tablas = [
        """"
         CREATE TABLE IF NOT EXISTS inventario(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             articulo TEXT NOT NULL,
             precio TEXT NOT NULL
         );
        """
        
    ]
    conexion = obtener_conexion
    cursor = conexion.cursor()
    for tabla in tablas:
        cursor.execute(tabla)
        
def principal():
 crear_tablas()
 menu = """
    a) Agrege un articulo
    b) Editar articulo
    c)Eliminar articulo
    d)Ver lista de articulo
    e)salir
    eliga:"""
 eleccion = ""
 while eleccion != "f":
        eleccion = input(menu)
        if eleccion == "a":
            articulo = input("Ingresa el articulo: ")
            posible_articulo = buscar_precio_articulo(articulo)
            if posible_articulo:
                print(f"el articulo '{articulo}' ya existe")
            else:
                precio = input("Ingresa el precio: ")
                agregar_articulo(articulo, precio)
                print("articulo agregado")
                
        if eleccion == "b":
            articulo = input("Ingresa la palabra que quieres editar: ")
            nuevo_precio = input("Ingresa el nuevo significado: ")
            editar_articulo(articulo, nuevo_precio)
            print("articulo actualizad")
       
        if eleccion == "c":
            articulo = input("Ingresa la palabra a eliminar: ")
            eliminar_articulo(articulo)
       
        if eleccion == "d":
            articulo = obtener_articulo()
            print("=== Lista de palabras ===")
            for articulo in articulo:
                print(articulo[0])
        
        if eleccion == "e":
            articulo = input(
                "Ingresa la palabra de la cual quieres saber el significado: ")
            precio = buscar_precio_articulo(articulo)
            if precio:
                print(f"El precio de '{articulo}' es:\n{precio[0]}")
            else:
                print(f"articulo '{articulo}' no encontrado")
                
                
def agregar_articulo(articulo, precio):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sentencia = "INSERT INTO inventario(articulo, precio) VALUES (?, ?)"
    cursor.execute(sentencia, [articulo, precio])
    conexion.commit()


def editar_articulo(articulo, nuevo_precio):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sentencia = "UPDATE inventario SET precio = ? WHERE articulo = ?"
    cursor.execute(sentencia, [nuevo_precio, articulo])
    conexion.commit()


def eliminar_articulo(articulo):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sentencia = "DELETE FROM inventario WHERE articulo = ?"
    cursor.execute(sentencia, [articulo])
    conexion.commit()


def obtener_articulo():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    consulta = "SELECT articulo FROM inventario"
    cursor.execute(consulta)
    return cursor.fetchall()


def buscar_precio_articulo(articulo):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    consulta = "SELECT precio FROM inventario WHERE articulo = ?"
    cursor.execute(consulta, [articulo])
    return cursor.fetchone()

if __name__ == '__main__':
    principal()