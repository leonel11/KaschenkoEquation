"""
@package parser
Module for parsing of data from json-file
"""

import json

class JsonParser:
    """
    @class JsonParser
    Main class of this module
    """

    def __init__(self, json_file):
        """
        Constructor
        @param json_file: path to json-file, which contains parameters of boundary-value problem
        """
        self.__json = json_file

    def pull_data(self):
        """
        Pull parameters from json-file
        @return: pulled parameters of json-file as a dictionary
        """
        with open(self.__json, 'r') as fjson:
            self.__data = json.load(fjson)
        return self.__data