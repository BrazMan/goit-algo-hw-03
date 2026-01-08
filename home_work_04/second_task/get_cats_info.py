import pathlib

cats_info_path = pathlib.Path(__file__).parent / 'cats_info.txt'

def get_cats_info(cats_info):
    list_dict_cats = []
    with open(cats_info_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                id, name, age = line.strip().split(',')
            except ValueError:
                print("Некоректний формат рядка у файлі. Пропускаємо цей запис.")
                continue
            try:
                age = int(age)
            except ValueError:
                print(f"Некоректне значення віку для кота з ID {id}: '{age}'. Пропускаємо цей запис.")
            list_dict_cats.append({
                'ID': id,
                'Name': name,
                'Age': int(age)
            })
    
    for item in list_dict_cats:
        print(item)
    return list_dict_cats        


try:
    get_cats_info(cats_info_path)
except FileNotFoundError or OSError as e:
    print("Файл не знайдено або неможливо відкрити. Перевірте шлях до файлу.")

