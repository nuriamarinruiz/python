#Ejercicio 6:
#Crear una función que genere un diccionario planta y lo añada a una lista.
#Crear una función que muestre los datos de todas las plantas creadas.
#Crear una función que modifique el diccionario planta.
#Crear una función que te diga los nombres de las plantas y el orden, eliges 1 y modifique esa planta con los nuevos datos.


print("Bienvenido a tu  diccionario Planta :")

plantas = {
  "Nombre": '',
  "Lugar": '',
  "Dias entre riegos": 0,
  "Tamaño": 0
}

 
    
try:
    plantas["Nombre"] = nombre = str(input("Escribe el nombre:"))
    
except:
    print("Tienes que introducir un dato valido")
        

try:
    plantas["Lugar"] = lugar = str(input("Escribe el lugar en el que se encuentra:"))
    
    
except:
    print("Tienes que introducir un dato valido")
       
        

try:
    plantas["Dias entre riegos"] = riegos = int(input("Escribe cada cuantos dias hay que regarla:"))
    
except:
    print("Tienes que introducir un dato valido")
        


try:
    plantas["Tamaño"] = tamaño = float(input("Escribe su altura media en cm:"))
    
except:
    print("Tienes que introducir un dato valido")
        
print(plantas)
