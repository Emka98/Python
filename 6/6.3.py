list_numbers = []

while True:
    list_numbers = [int(x) for x in input('Podaj 5 wartości oddzielonych spacją: ').split()]
    if len(list_numbers) == 5:
        break
         
odd = sum(map(lambda x: x % 2, list_numbers))
print(f"You entered even {5 - odd} and {odd} odd numbers.")







