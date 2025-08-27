napis = ""

while len(napis) < 5:
    tmp = input("Enter number in range 0 - 9: ")
    if tmp in "0123456789" and len(tmp) == 1:
        napis += tmp
        
number1, number2 = int(napis), int("".join(reversed(napis)))

print(f"Number entered: {number1}")
print(f"Number reversed: {number2}")
print(f"Sum of {number1} + {number2} = {number1 + number2}")