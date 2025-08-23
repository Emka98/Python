import re

consonats = "b, c, d, f, g, h, j, k, l, m, n, ń, p, r, s, t, w, z"
volves = "a, e, i, o, u, y"
lista = []

while len(lista) < 10:
    tmp = input("Enter letter: ")

    if re.search(tmp,consonats):
        lista.append(tmp)
    elif re.search(tmp,volves):
        lista.insert(0,tmp)
    elif tmp == "*" and len(lista) > 0:
        lista.pop(0)
    elif tmp == "#" and len(lista) > 0:
        lista.pop()
    elif tmp == "!":
        break
    elif tmp == "&":
        print(lista)