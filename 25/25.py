V = []
while True:
    V.append(int(input("Enter intiger number: ")))
    V.append(int(input("Enter intiger number: ")))
    if V[-1] * V[-2] <= 1000:
        V.append(V[-1] * V[-2])
    else:
        break
print(V)