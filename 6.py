# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.

from collections import namedtuple
import argparse
import os
from pathlib import Path
import logging

logging.basicConfig(filename='log_task6.log',
                    encoding='utf-8',
                    format='{levelname} - {asctime} функция "{funcName}()"'
                           ' строка {lineno} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def psrser_directory(directors: str):
    try:
        os.chdir(directors)
        res = []
        p = Path(Path.cwd())
        for i in p.iterdir():
            list_1 = str(i).split("/")
            list_2 = []
            name_file = list_1[-1].split('.')[0]
            list_2.append(name_file)
            if len(list_1[-1].split('.')) == 2:
                type_file = list_1[-1].split('.')[1]
                list_2.append(type_file)
            list_2.append(i.is_dir())
            dir_file = list_1[-3]
            list_2.append(dir_file)
            res.append(list_2)
        for i in res:
            Dir = namedtuple("Dir", ['name_file', 'type_file', 'dir_flag', 'direct'])
            if len(i) == 4:
                dir1 = Dir(*i)
                logger.info(dir1)
            elif i[1] == True:
                dir2 = Dir(name_file=i[0], type_file="directory", dir_flag=i[1], direct=i[2])
                logger.info(dir2)
            else:
                dir3 = Dir(name_file=i[0], type_file=None, dir_flag=i[1], direct=i[2])
                logger.info(dir3)
        return res
    except Exception:
        logger.critical(f"Ошбика пути. программа не может найти {directors} путь")
        print(f"Ошбика пути. программа не может {directors} такой путь")


parser = argparse.ArgumentParser(description='Принимаем на вход путь по директории на ПК и собираем информацию')
parser.add_argument('dir', type=str, default=os.getcwd())
arg = parser.parse_args()
psrser_directory(arg.dir)

os.chdir("/home/aleksander/PycharmProjects/pythonProject1/GB/Task15")
os.getcwd()
with open('log_task6.log', 'r', encoding='utf-8') as log_file:
    print(log_file.read())
