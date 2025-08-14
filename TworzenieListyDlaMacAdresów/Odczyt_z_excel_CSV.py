import pandas as pd

def odczyt_excel(pathToFile):
    df = pd.read_csv(pathToFile, sep=';', header=0)

    #Remove empty rows
    df = df.dropna(subset=['NUMER FABRYCZNY', 'MAC ADRES'])

    #Change type to dict
    slownik_mac = df.set_index('NUMER FABRYCZNY')['MAC ADRES'].to_dict()
    
    return slownik_mac