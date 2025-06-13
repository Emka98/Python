import os
import hashlib
import shutil


def gen_file(size: int, path: str) -> None:
    with open(path, 'wb') as f:
        f.write(os.urandom(size * 1024 * 1024))
    return


def calculate_md5(path_to_file: str) -> str:
    hash_md5 = hashlib.md5()
    with open(path_to_file, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def path_maker(file_name) -> str:
    # Ściezka do pliku na Fill Gun
    path_to_fill_gun_file = '/media/{}/{}/{}'.format(os.getlogin(), name_device, file_name)
    path_to_com_place_file = '/home/{}/Desktop/{}'.format(os.getlogin(), file_name)

    return path_to_fill_gun_file, path_to_com_place_file


def file_remover(path_to_file: str) -> None:
    os.remove(path_to_file)
    return


def copy(file_to_copied: str, new_place: str) -> None:
    shutil.copy2(file_to_copied, new_place)
    return


def check_file(file_path: str) -> bool:
    return os.path.exists(file_path)


# Setup
size = 500
file_name = 'test.bin'
name_device = 'FG'

try:
    fill_path, com_path = path_maker(file_name)

    if check_file(fill_path):
        file_remover(fill_path)

    if check_file(com_path):
        file_remover(com_path)

    try:
        gen_file(size, com_path)
        copy(com_path, fill_path)

        try:
            sum_com = calculate_md5(com_path)
            sum_fill = calculate_md5(fill_path)

            if sum_com == sum_fill:
                print(f'''\nGratulację i owacje sumy kontrolne plików są takie same!!!\n
Suma pliku {com_path} -> {sum_com}
Suma pliku {fill_path} -> {sum_fill}\n''')

            else:
                print(f'''\nPizda z dziobem plik sumy kontrolne są różne!!!\n
Suma pliku {com_path} -> {sum_com}
Suma pliku {fill_path} -> {sum_fill}\n''')

            try:
                file_remover(fill_path)
                file_remover(com_path)
                if check_file(fill_path) and check_file(com_path):
                    print(f'''\nPoprawnie usunięto pliki:\n
{com_path}
{fill_path}\n''')

            except:
                print('Błąd usuwania pliku')
        except:
            print(f'Problem z policzeniem sumy kontrolnej plików')
    except:
        print(f'Problem z wygenerowaniem lub przekopiowaniem pliku {file_name}')
except:
    print(f'''Problem z usunięciem starych plików testowych lub utworzenie ścieżki do katalogów.
{fill_path}
{com_path}
''')