while True:    
    number = int(input("Enter an integer "))
    if number%3 == 0 and number%5 == 0:
        print("The number is divisible by 3 and 5")
        break
    elif number%3==0 and number%5 != 0:
        print("The number is divisible by only 3")
        break
    elif number%3 != 0 and number%5 == 0:
        print("The number is divisible by only 5")
        break

    

