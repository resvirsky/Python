elements = [89, 23, 33, 45, 10, 12, 45, 45, 45]
ordered_elements=[]

while elements:
    minimo=elements[0]
    for x in elements:
        if x < minimo:
            minimo = x
    ordered_elements.append(minimo)
    elements.remove(minimo)

print ordered_elements
