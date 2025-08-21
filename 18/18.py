sum = 0
while True:
    tmp = int(input("Enter your number: "))
    print(tmp*2)
    if tmp in range(1,11):
        print(sum)
        break
    sum += tmp*2