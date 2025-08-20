a = b = c = -1
while (a < 0 or b < 0 or c < 0):
  a, b, c = [int(x) for x in input(
    'Please provide 3 positive numbers separated by spaces, that is = a b c: ').split()]
suma = a + b + c - max(a, b, c)
for i in range(max(a, b, c)):
  print(suma, end=' ')