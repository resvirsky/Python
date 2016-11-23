data_list = [67, 45, 2, 13, 1, 998]
new_list = []

while data_list:
    minimum = data_list[1]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    

print new_list
