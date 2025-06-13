import os

ilosc_adresow = int(input("Podaj ilośc adresów które chcesz pingować: "))
lista_adresow = []

for i in range(ilosc_adresow):
    lista_adresow.append(input("Podaj {} adres IP: ".format(i+1)))

for adres in lista_adresow:
    try:
        print("Pingowanie adresu {} dla prędkości {}".format(adres))
        os.system("ping -c 10 ")
    except:
        print("Bład podczas pingowania adresu {}".format(adres))