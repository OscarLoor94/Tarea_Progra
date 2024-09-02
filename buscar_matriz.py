#Creamos la lista
lista = [
    [8,7,6],
    [10,11,7],
    [8,9,4]
    ]

#Declaramos la funcion buscar con párametros x
def busca(l,x):

    for i  in range(len(lista)):  #Recorremos con el iterador i las filas
        for j in range(len(lista[i])) : #Iterador j recorremos las columnas
          if lista[i][j]  == x :  #Comparamos si las posiciones en la fila y columnas son iguales al numero que buscamos

              return i,j # retornamos

    return None  # si no encuentra el numero que estamos buscando en la lista retornamos  None
print("LISTA")  #Imprimimos las listas
for i in lista :
    print(i)



numero = int(input("Que numero desea buscar: "))
print("El numero esta en la posición ",busca(lista,numero))



