dvideBy6 = 0
listdvideBy6 = []

dvideBy6with7 = 0
listdvideBy6with7 = []

for i in range(1, 1001):
    if i % 6 == 0:
        listdvideBy6.append(i)
        dvideBy6 += 1
        if "7" in str(i):
            listdvideBy6with7.append(i)
            dvideBy6with7 += 1
            
print(f"List of {dvideBy6} numbers divded by 6: {listdvideBy6}")
print(f"List of {dvideBy6with7} numbers divded by 6 with 7: {listdvideBy6with7}")