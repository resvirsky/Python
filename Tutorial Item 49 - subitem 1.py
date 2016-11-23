elements = [67, 45, 2, 13, 1, 998]
ordered_elements=[]

while elements:
    minimo=elements[0]
    for x in elements:
        if x < minimo:
            minimo = x
    ordered_elements.append(minimo)
    elements.remove(minimo)

print ordered_elements
