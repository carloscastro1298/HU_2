
inventario = []

def agregar_producto():
    print("\n--- Agregar producto ---")
    
    nombre = input("Nombre del producto: ")
    
    try:
        precio = float(input("Precio: "))
    except:
        print("Precio inválido")
        return
    
    try:
        cantidad = int(input("Cantidad: "))
    except:
        print("Cantidad inválida")
        return
    
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    
    inventario.append(producto)
    print("Producto agregado correctamente")


def mostrar_inventario():
    print("\n--- Inventario ---")
    
    if len(inventario) == 0:
        print("El inventario está vacío")
        return
    
    for producto in inventario:
        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

def calcular_estadisticas():
    print("\n--- Estadísticas ---")
    
    if len(inventario) == 0:
        print("No hay datos para calcular")
        return
    
    valor_total = 0
    total_productos = 0

    
    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        total_productos += producto["cantidad"]
    
    print(f"Valor total del inventario: {valor_total}")
    print(f"Cantidad total de productos: {total_productos}")



while True:
    print("\n===== MENÚ =====")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")
    

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
