lista=[89, 23, 33, 45, 10, 12, 45, 45, 45]
lista_ordenada=[]

while lista:
    minimo=lista[0]
    for x in lista:
        if x < minimo:
            minimo = x
    lista_ordenada.append(minimo)
    lista.remove(minimo)
print lista_ordenada
