inventario= []

while True:
    print ("---MENU---")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadisticas")
    print("4. Salir")

    opcion = input ("Escoge una opcion: ")
    if opcion == "1": 
        nombre= input ("Nombre del producto:")
        precio= int (input("Precio: "))
        cantidad= int(input("Cantidad: "))

        producto={
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        inventario.append(producto)
        print("Producto guardado!")
    elif opcion == "2":
        if len (inventario) == 0:
            print("El inventario esta vacio!")
        else:
            for p in inventario:
                print("Producto: ", p["nombre"])
                print("Precio: ", p["precio"])
                print("Cantidad: ", p["cantidad"])
    elif opcion == "3":
        if len (inventario) == 0:
            print("No hay productos en el inventario!")
        else:
            total= 0
            for p in inventario:
                total = total * (p["precio"])
    elif opcion == "4":