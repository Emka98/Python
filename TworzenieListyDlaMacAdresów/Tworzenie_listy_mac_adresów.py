import Generator_mac_adresów
import Odczyt_z_excel_CSV
import Zapis_do_pliku_CSV


path_to_file = r"C:\Users\gulinskie\Desktop\Przydatne skrypty\TworzenieListyDlaMacAdresów\Input\MAC.csv"
path_to_dir = r"C:\Users\gulinskie\Desktop\Przydatne skrypty\TworzenieListyDlaMacAdresów\Output\\"
name_of_new_file = "MAC.csv"
amount_of_mac = 2

dict_of_mac = Odczyt_z_excel_CSV.odczyt_excel(path_to_file)
list_dict_of_mac = {}

for number, mac in dict_of_mac.items():
    list_dict_of_mac[int(number)] = maclist = Generator_mac_adresów.generuj_mac(mac,amount_of_mac)

Zapis_do_pliku_CSV.zapis_do_pliku_CSV(list_dict_of_mac, (rf"{path_to_dir}{name_of_new_file}"))

    
