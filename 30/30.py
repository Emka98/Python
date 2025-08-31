list_mass = [1,1]
rounds = 13

for i in range(rounds):
    if i > 1:
        list_mass.append(list_mass[i-2] + list_mass[i-1])
    print(f"Round: {i+1} mass of Blob: {list_mass[i]} ")