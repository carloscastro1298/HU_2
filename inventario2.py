# Lista donde se guardarán los productos
inventario = []

# -----------------------------
# Función para agregar producto
# -----------------------------
def agregar_producto():
    print("\n--- Agregar producto ---")
    
    nombre = input("Nombre del producto: ")
    
    # Validación de precio
    try:
        precio = float(input("Precio: "))
    except:
        print("Precio inválido")
        return
    
    # Validación de cantidad
    try:
        cantidad = int(input("Cantidad: "))
    except:
        print("Cantidad inválida")
        return
    
    # Crear diccionario del producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    
    # Agregar a la lista
    inventario.append(producto)
    print("Producto agregado correctamente")


# -----------------------------------
# Función para mostrar el inventario
# -----------------------------------
def mostrar_inventario():
    print("\n--- Inventario ---")
    
    if len(inventario) == 0:
        print("El inventario está vacío")
        return
    
    # Recorrer lista con for
    for producto in inventario:
        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")


# -----------------------------------
# Función para calcular estadísticas
# -----------------------------------
def calcular_estadisticas():
    print("\n--- Estadísticas ---")
    
    if len(inventario) == 0:
        print("No hay datos para calcular")
        return
    
    valor_total = 0
    total_productos = 0
    
    # Recorrer inventario
    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        total_productos += producto["cantidad"]
    
    print(f"Valor total del inventario: {valor_total}")
    print(f"Cantidad total de productos: {total_productos}")


# -----------------------------
# Bucle principal (menú)
# -----------------------------
while True:
    print("\n===== MENÚ =====")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")
    
    # Validación con condicionales
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        calcular_estadisticas()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intenta de nuevo")
        

# -------------------------------------------------
# RESUMEN:
# Este programa permite gestionar un inventario usando:
# - Listas y diccionarios
# - Funciones
# - Bucles (while y for)
# - Condicionales (if, elif, else)
# - Validación de datos
# -------------------------------------------------
