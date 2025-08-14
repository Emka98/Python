import csv

def zapis_do_pliku_CSV(slownik, file):
    with open(file, mode='w', newline='', encoding='utf-8') as plik:
        writer = csv.writer(plik, delimiter=';')
        writer.writerow(['NUMER FABRYCZNY', 'MAC ADRES'])

        for numer, mac_lista in slownik.items():
            for mac in mac_lista:
                writer.writerow([numer, mac])