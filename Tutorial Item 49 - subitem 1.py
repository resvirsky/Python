lista=[67, 45, 2, 13, 1, 998]
lista_ordenada=[]

while lista:
    minimo=lista[0]
    for x in lista:
        if x < minimo:
            minimo = x
    lista_ordenada.append(minimo)
    lista.remove(minimo)
print lista_ordenada
