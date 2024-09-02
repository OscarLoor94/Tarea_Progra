


print("")
print("LISTA")

#ORDENAR LISTA
def bubble_sort(fila):

    n = len(fila) # Declaramos la variable que cuente nuestra fila
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

listas = [
    [8,7,6],
    [10,11,7],
    [8,9,4]
    ]


# Imprimimos la lista original
for fila in listas :
  print(fila)



bubble_sort(listas[1])  #Definimos la función y llenamos los parametros
# Imprimimos  la lista  después de ordenar, y seleccionamos la fila
print("\nLISTA ORDENADA")
for fila in listas:
    print(fila)
