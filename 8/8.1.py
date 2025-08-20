def show_result (a, b, operator):
    try: 
        print(f"{a} {operator} {b} = {eval(f'{a} {operator} {b}')}")
        if (operator == "-" or operator == '/') and a != b:
            print(f"{b} {operator} {a} = {eval(f'{b} {operator} {a}')}")
    except:
        print("You can't divide by 0")

try:
    sign = "* + – /"
    a = float(input("Enter folating number: "))
    b = float(input("Enter folating number: "))

    operator = input(f"Enter one of them: [{sign}].")

    if operator in sign:
        show_result(a, b, operator)
    else:
        print("You entered the random operator")
except:
    print("Problem with entered number.")