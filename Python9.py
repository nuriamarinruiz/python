#Ejercicio 9

instrumentos = set()

def agregarInstrumento():
    instrumento = input("Introduce un instrumento musical para agregar: ")
    instrumentos.add(instrumento)
    print(instrumento + " ha sido agregado a instrumentos musicales.")

def eliminarInstrumento():
    instrumento = input("Introduce un instrumento musical para eliminar: ")
    if instrumento in instrumentos:
        instrumentos.remove(instrumento)
        print(instrumento + " ha sido eliminado de instrumentos musicales.")
    else:
        print(instrumento + " no se encontró en instrumentos musicales.")

while True:
    print("\nOpciones:")
    print("1. Agregar instrumento")
    print("2. Eliminar instrumento")
    print("3. Mostrar instrumentos")
    
    opcion = input("Elige una opción (1/2/3): ")
    
    if opcion == '1':
        agregarInstrumento()
    elif opcion == '2':
        eliminarInstrumento()
    elif opcion == '3':
        print("\nInstrumentos musicales en el conjunto:")
        for instrumento in instrumentos:
            print(instrumento)
    else:
        print("Opción no válida. Por favor, elige una opción válida (1/2/3).")


