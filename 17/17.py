# Way 1
list = []
tmp1 = 6
tmp2 = 2

for i in range(101):
    if i % 2 == 0:
        list.append(tmp1)
        tmp1 = tmp1 + 2       
    else:
        list.append(tmp2)
        tmp2 = tmp2 + 1
print(list)

#Or we can just show it in row:

for i in range(101):
    if i % 2 == 0:
        list.append(tmp1)
        tmp1 = tmp1 + 2       
    else:
        list.append(tmp2)
        tmp2 = tmp2 + 1
print(list)

#Way 2 (I can done easier
start1, start2 = 6, 2
step1, step2 = 2, 1

for i in range(1, 51):
  print(start1, start2)
  start1, start2 = start1 + step1, start2 + step2