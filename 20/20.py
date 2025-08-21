list1 = []
list2 = []

while (len(list1) < 10 or len(list2) < 10):
    try:
        tmp = int(input("Enter number: "))
    except:
        print("Check entered vaule")
    if len(list1) < 10:
        list1.append(tmp)
        if tmp % 2 == 0:
            list2.append(tmp)
    else:
        list2.append(tmp)
        
print(f"List 1 {list1}")
print(f"List 2 {list2}")