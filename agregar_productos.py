def agregar_producto(producto):
    nombre = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        return False
    try:
        precio = float(input("ingrese el precio untitario del producto: "))
        producto [nombre.upper()] = precio
    except ValueError:
        print("Error: Debe ingresar un precio valido")
    return True