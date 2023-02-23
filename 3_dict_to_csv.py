"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

list1 = [
        {'name': 'Мария', 'age': 27, 'job': 'Scientist'}, 
        {'name': 'Александр', 'age': 33, 'job': 'Programmer'}, 
        {'name': 'Марина', 'age': 45, 'job': 'Big boss'},
    ]

def main():

    with open('export.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in list1:
            writer.writerow(user)

if __name__ == "__main__":
    main()
