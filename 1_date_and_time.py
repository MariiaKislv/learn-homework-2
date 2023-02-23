"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, timedelta

def print_days():
    
    today = datetime.today()
    delta_1 = timedelta(days=1)
    delta_2 = timedelta(days=30)
    yesterday = (today - delta_1).strftime('%Y/%m/%d')
    today_2 = today.strftime('%Y/%m/%d')
    last_month = (today - delta_2).strftime('%Y/%m/%d')
    print(f'Вчера: {yesterday}, Сегодня: {today_2}, 30 дней назад: {last_month}')

def str_2_datetime(date_string):
    
    date_dt = datetime.strptime(date_string, "%m/%d/%y %H:%M:%S.%f")
    return date_dt


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
