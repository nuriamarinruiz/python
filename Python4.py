#Ejercicio 4:
#Pedir por consola qué ejercicio creado hasta el momento se quiere ejecutar.


def ej1():

    nombre = str(input("Hola, escribe tu nombre:"))
    edad = int(input("Escribe tu edad:"))
    print("Estos son los dias que has vivido", edad*365)


def ej2():

    print("Vamos a calcular el área de un triángulo")
    base = float(input("Escribe la base:"))
    altura = float(input("Escribe la altura:"))

    if base < 0 or altura < 0 :
        print("no puedes poner un numero negativo")
    else:
        print("Este es el area del triangulo en cm :", ((base*altura)/2))

def ej3():

    print("Vamos a crear una lista de numeros")

    list = [ ]
    for i in range(6):  
    
        try:
            numeroAñadido = int(input("Escribe un numero :"))
            list.append(numeroAñadido)
    
        except:
            print("Tienes que introducir un numero")
        
        
    list.sort()
    print(list)




respuesta = input("Hola! Dime que número de ejercicio es el que quieres ejecutar")

if respuesta == "1" :
    ej1()

if respuesta == "2":
    ej2()

if respuesta =="3":
    ej3()