list = []
counter = 0

for i in range(1, 201):
    list.append(i)
    if i >= 6 and 1000 > ((list[i-6]+list[i-5]+list[i-4]+list[i-3]+list[i-2]+list[i-1])) > 800:
        counter += 1

print(f"You have {counter} numbers where the sum exceeds 800 but does not exceed 1000")