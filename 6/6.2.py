list_numbers = []

print("Enter 5 intigers.")

while len(list_numbers) < 5:
    try: 
        list_numbers.append(int(input("Enter initiger: ")))
    except:
        print("Check entered values.")
        
odd = sum(map(lambda x: x % 2, list_numbers))
print(f"You entered even {5 - odd} and {odd} odd numbers.")