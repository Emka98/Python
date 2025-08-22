list = []
while True:
    list.append(int(input("Enter a number if you want to end enter 2 same number ")))
    if len(list) >= 2 and list[-2] == list[-1]: break