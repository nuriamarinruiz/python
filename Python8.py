#Ejercicio 8
asignaturas = []

while True:

    asignatura = input("Introduce una asignatura o escribe 'fin' para terminar: ")

    if asignatura == 'fin':
        break
    
   
    asignaturas.append(asignatura)

print("\nAsignaturas introducidas:")
for asignatura in asignaturas:
    print(asignatura)

