#Ejercicio 5:
#Crear un diccionario Planta con diversos atributos: Nombre, Lugar, días entre riegos, tamaño...
#Validar cada tipo de dato que se meta por consola.


print("Bienvenido a tu diccionario Planta :")

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
