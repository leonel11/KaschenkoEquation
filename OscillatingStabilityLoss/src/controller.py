"""
@package contoller
Связующий модуль-контроллер
"""

from jsonparser import JsonParser
from calculator import Calculator
import numpy as np

## @class Controller
class Controller:
    """
    @class Controller
    Основной класс данного модуля
    """

    def __init__(self, json_file, delay):
        """
        Конструктор класса
        @param json_file: путь до json-файла с параметрами задачи
        """
        self.__jp = JsonParser(json_file)
        self.__params = self.__jp.pull_data()
        self.__delay = delay

    def run(self):
        """
        Запуск расчетов и отображение полученных результатов
        """
        gs = np.linspace(self.__params['gamma']['first'], self.__params['gamma']['last'],
                         self.__params['gamma']['steps']).tolist()
        calc = Calculator(gs[0], self.__params['alpha'], self.__params['omega'],
                          self.__delay, self.__params['shift'], self.__params['eps'])
        calc.run()
        crits = calc.get_critical_values()