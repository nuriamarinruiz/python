#Ejercicio 7
#Crear una tupla
tuplaInicial = (1, 2, 3, 4, 5)


def modificarTupla(tupla, indice, nuevoValor):
    
    lista= list(tupla)
    
    if indice >= 0 and indice < len(lista):
        lista[indice] = nuevoValor
    
    tuplaModificada = tuple(lista)
    
    return tuplaModificada


indice = 2
nuevoValor = 10
tuplaFinal = modificarTupla(tuplaInicial, indice, nuevoValor)


print("Tupla original:", tuplaInicial)
print("Tupla modificada:", tuplaFinal)
