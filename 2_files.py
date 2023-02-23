"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.droсpbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    
    with open ('referat.txt', 'r', encoding='utf-8') as file:
        words_amount = 0
        content = []
        line_number = 0
        for line in file:
            line_number += 1
            print(f'Длина строки {line_number}: {len(line)}')
            words_amount += len(line.split())
            content.append(line.replace('.', '!'))
        print(f'Количество слов в текстe: {words_amount}')

        with open ('referat2.txt', 'w', encoding='utf-8') as file2:

            file2.write(''.join(content))
        

if __name__ == "__main__":
    main()
