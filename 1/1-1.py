times = 3
repats = 0
i = 1
list_numbers = []

while True:
    if repats == times:
        break
    else:
        try:
            tmp = int(input(f"Enter {len(list_numbers)+1} non-negative integers: "))
        except:
            print("Incorrect character was entered")
        if tmp >= 0:
            list_numbers.append(tmp)
            repats += 1
        else:
            print("Negative integers was entered")
        
tmp = max(list_numbers)
list_numbers.remove(tmp)
sum_numbers = sum(list_numbers)

i = 0
for i in range(tmp):
    print(sum_numbers)