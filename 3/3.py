try:
    a = int(input("Enter intiger: "))
    if (a % 3 == 0 and a % 5 == 0):
        print("Numeber is divided by 3 and 5")
    elif (a % 3 == 0 and a % 5 != 0):
        print("Numeber is divided by 3")
    elif (a % 3 != 0 and a % 5 == 0):
        print("Numeber is divided by 5")
    else:
        print("Numeber isn`t divided by 3 and 5")  
except:
    print("Entered value isn`t intiger")