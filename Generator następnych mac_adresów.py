import re

def generuj_mac(mac_adres, ilosc):
    # Sprawdzenie poprawności adresu MAC
    if not re.match(r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$", mac_adres):
        raise ValueError("Niepoprawny format adresu MAC")
   
    # Konwersja adresu MAC na liczbę
    mac_int = int(mac_adres.replace(":", ""), 16)
   
    # Generowanie kolejnych adresów MAC
    mac_list = []
    for i in range(ilosc):
        nowy_mac = mac_int + i
        mac_hex = f"{nowy_mac:012X}"  # Konwersja do 12-znakowego heksadecymalnego formatu
        mac_formatowany = ":".join(mac_hex[i:i+2] for i in range(0, 12, 2))  # Formatowanie adresu MAC
        mac_list.append(mac_formatowany)
   
    return mac_list


mac_poczatkowy = input("Podaj mac-adresów początkowy: ")
ilosc_potrzebnych = int(input("Podaj ilość potrzbnych mac-adresów: "))
nowe_adresy = generuj_mac(mac_poczatkowy, ilosc_potrzebnych)
numeracja = 1

print("Wygenerowane adresy MAC:")
for mac in nowe_adresy:
    print(f"{numeracja} - {mac}")
    numeracja += 1
