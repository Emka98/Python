while True:
    try:
        a1, a2, a3, a4, a5 = [float(x) for x in
                            input('Enter 5 values separated by a space ').split()]
        if (a5 == 0):
            print(f'To się nie uda, a5={a5} uniemożliwia dzielenie.')
        else:
            print(f'Result =>', (((a1 + a2) * a3) - a4) / a5)
            break
    except:
        print("Check all entered values.")