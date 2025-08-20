element_of_sequence = 100
list_elements = [3, 1, 2, 1]

for i in range(element_of_sequence, 0, -1):
    print(f"{list_elements[i%4]}")