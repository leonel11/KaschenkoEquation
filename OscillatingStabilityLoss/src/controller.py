"""
@package contoller
Module-controller
"""

from jsonparser import JsonParser
from calculator import Calculator
import numpy as np

## @class Controller
class Controller:
    """
    @class Controller
    Main class of this module
    """

    def __init__(self, json_file, delay):
        """
        Constructor
        @param json_file: path to json-file, which contains parameters of boundary-value problem
        """
        self.__jp = JsonParser(json_file)
        self.__params = self.__jp.pull_data()
        self.__delay = delay

    def run(self):
        """
        Compute critical values of parameters and their visualization
        """
        gs = np.linspace(self.__params['gamma']['first'], self.__params['gamma']['last'],
                         self.__params['gamma']['steps']).tolist()
        crits = dict()
        # enumeration values of gamma for the search of critical values
        for gamma in gs:
            calc = Calculator(gs[0], self.__params['omega'], self.__params['alpha'],
                              self.__delay, self.__params['shift'], self.__params['eps'])
            print('\u03B3 = {:.4f}'.format(gamma))
            res_calc = calc.get_critical_values()
            # addition computed critical values
            if res_calc:
                dict_key = '{:.4f}'.format(gamma)
                crits[dict_key] = res_calc
        # TODO: unroll dictionary
        # TODO: save unrolled dictionary to csv
        # TODO: print results
        pass