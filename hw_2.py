# Взять любую задачу и настроить в ней запуск скрипта с параметрами.
# (используем Пайчарм и модуль argparse)
import argparse


def func(txt: str) -> dict:
    dict_txt = {}
    for key in txt:
        if key not in dict_txt:
            dict_txt[key] = 1
        elif key in dict_txt:
            dict_txt[key] += 1
    return dict_txt

parser = argparse.ArgumentParser(description="Принимаем строку и делаем подсчет количества букв в строке")
parser.add_argument("-txt", metavar='txt', type=str, default='Hello World')
arg = parser.parse_args()

# func(arg.txt)
# txt = "saswwwa qwqw rssrre"
print(func(arg.txt))
