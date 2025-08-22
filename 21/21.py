try:
    a, b, c, d, e = [int(x) for x in input('Enter 5 numbers separeted by space').split()]
except:
    print("Check entered values!")
if a < b < c < d < e:
    print("The entered numerical sequence is ascending")