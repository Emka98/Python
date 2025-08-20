numbers_5_11 = 0
numbers = 0 

for i in range(1, 121, 1):
    if i % 11 == 0 and i % 5 == 0:
        print(i)
        numbers_5_11 += 1
    else:
        numbers += 1

print(f"Printed numbers: {numbers_5_11} and skiped numbers {numbers}")
        
    