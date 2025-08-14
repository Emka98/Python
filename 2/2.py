try:
    a = int(input("Enter intiger:"))
    if a % 2 == 0:
        print(f"That intiger {a} is even")
    else:
        print(f"That intiger {a} isn`t even")
except:
    print("You entered something other than an integer")