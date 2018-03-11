"""
@package parser
Модуль для распарсивания данных из json-файла
"""

import json

class JsonParser:
    """
    @class JsonParser
    Основной класс данного модуля
    """

    def __init__(self, json_file):
        """
        Конструктор класса
        @param json_file: путь до json-файла с параметрами задачи
        """
        self.__json = json_file

    def pull_data(self):
        """
        Вытягивание данных из json-файла
        @return: вытянутые из json-файла параметры в виде словаря
        """
        with open(self.__json, 'r') as fjson:
            self.__data = json.load(fjson)
        return self.__data