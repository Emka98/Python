a = b = c = -1
while (a < 0 or b < 0 or c < 0):
  a = int(input('Podaj liczbę a: '))
  b = int(input('Podaj liczbę b: '))
  c = int(input('Podaj liczbę c: '))

if a > b:
  maks = a
else:
  maks = b
if maks < c:
  maks = c

suma = a + b + c - maks
while maks:
  print(suma, end=' ')
  maks -= 1
print()
