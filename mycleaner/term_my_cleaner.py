import sys
import shutil
import os
from pathlib import Path

try:
    from mycleaner import cleaner, smart
except ModuleNotFoundError:
    import cleaner
    import smart


COLUMNS, _ = shutil.get_terminal_size()


def get_path():
    if len(sys.argv) > 1:
        return [path for path in sys.argv[1:] if Path(path).exists() and (Path(path).is_file() or Path(path).is_dir())]


def make_path_obj(path_list):
    return [smart.PathObj(path_obj) for path_obj in path_list]


def logo_dec(func):
    def deco():
        print('My Cleaner'.center(COLUMNS, '='))
        print('Утилита для затирания, обнуления, удаления файлов'.center(COLUMNS, ' '))
        print('Aleksandr Suvorov | myhackband@ya.ru'.center(COLUMNS, '-'))
        print(''.center(COLUMNS, '='))
        func()
        print(''.center(COLUMNS, '='))
        print('Программа завершена'.center(COLUMNS, '-'))
    return deco


@logo_dec
def main():
    print('Добавляем пути...')
    path_list = get_path()
    if path_list:
        print(f'Добавлено путей: {len(path_list)}')
        print('Ищем файлы...')
        obj_list = make_path_obj(path_list)
        my_cleaner = cleaner.Cleaner()
        num_files = sum([len(files) for path in path_list for p, _, files in os.walk(path)])
        print(f'Найдено файлов: {num_files}')
        print(''.center(COLUMNS, '='))
        while True:
            print('Выберите нужное действие:\n0. Выход\n1. Уничтожение\n2. Обнуление\n3. Обычное удаление')
            print(''.center(COLUMNS, '-'))
            try:
                user_input = int(input('Ввод: '))
                if user_input not in [0, 1, 2, 3]:
                    raise ValueError
                my_cleaner.shreds = int(input('Введите количество проходов для перезаписи: '))
            except ValueError:
                print(''.center(COLUMNS, '-'))
                print('Ошибка ввода!')
                continue
            else:
                for obj in obj_list:
                    print(f'Работаем с: {obj.path}'.center(COLUMNS, '='))
                    for file in obj.get_files():
                        if user_input == 1:
                            print(f'Уничтожаем файл: {file}')
                            my_cleaner.shred_file(file)
                        elif user_input == 2:
                            print(f'Обнуляем файл: {file}')
                            my_cleaner.zero_file(file)
                        elif user_input == 3:
                            print(f'Удаляем файл: {file}')
                            my_cleaner.del_file(file)
            print('Работа завершена'.center(COLUMNS, '='))
            print(f'Было обработано файлов: {my_cleaner.count_del_files + my_cleaner.count_zero_files}')
            break
    else:
        print('Ошибка! Пути не найдены')


if __name__ == '__main__':
    main()
