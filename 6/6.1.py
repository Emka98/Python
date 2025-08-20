list_numbers = []
even = 0

print("Enter 5 intigers.")

while len(list_numbers) < 5:
    list_numbers.append(int(input("Enter initiger: ")))

for x in list_numbers:
    if x % 2 == 0:
        even += 1

print(f"You entered even {even} and {5-even} odd numbers.")