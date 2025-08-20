try:
    number = int(input("Enter intiger: "))
except:
    print("You entered wrong number.")
    
if number > 0:
    number += 1
elif number < 0:
    number -= 1

if number % 2 == 0: text = "even" 
else: text = "odd"

print(f"Entered nmuber {number} {text}")