#introduction
print("Calculator of expresion: (((a1+a2)*a3)-a4)/a5")

#Get value of variables a1>>a5
dictA = {}
while (len(dictA) < 5):
    try:
        dictA[f"a{len(dictA)+1}"] = float(input(f"Enter floating point of a{len(dictA)+1}: "))
        if len(dictA) == 5 and dictA["a5"] == 0:
            print("You can't enetere a5 like 0 change value")
            dictA.popitem()
    except:
        print("You didn't eneter floating point")

#show result of expresion
print("((({a1}+{a2})*{a3})-{a4})/{a5} = {result}".format(a1 = dictA["a1"], 
                                                         a2 = dictA["a2"],
                                                         a3 = dictA["a3"],
                                                         a4 = dictA["a4"],
                                                         a5 = dictA["a5"],
                                                         result = (((dictA["a1"]+dictA["a2"])*dictA["a3"])-dictA["a4"])/dictA["a5"]))