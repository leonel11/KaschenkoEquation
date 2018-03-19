"""
@package results
Module for output results
"""

from pathlib import Path
import pandas as pd
from os import path
from utils import create_dir, results_filename
import matplotlib.pyplot as plt

RESULT_DIR = path.join(Path(__file__).parents[1], path.basename(__file__).split('.')[0])

class Results:

    def __init__(self, crits, delay, shift):
        self.__data = self.__criticals_to_dataframe(crits)
        self.__filename = results_filename(delay, shift)

    def __criticals_to_dataframe(self, crits):
        df = pd.DataFrame(columns=['gamma', 'omega', 'alpha'])
        for gamma in crits.keys():
            for omega in crits[gamma].keys():
                for alpha in crits[gamma][omega]:
                    row = list(map(float, [gamma, omega, alpha]))
                    # TODO: strange way to add row
                    df.loc[len(df)] = row
        return df

    def __save_to_csv(self):
        csv_name = path.join(RESULT_DIR, self.__filename + '.csv')
        self.__data.to_csv(csv_name, sep=';', float_format='%.4f', index=False)

    def __save_to_img(self):
        img_name = path.join(RESULT_DIR, self.__filename + '.png')
        # TODO: Correct the borders of plot to see all labels right
        plt.scatter(self.__data['gamma'], self.__data['alpha'], s=0.2)
        plt.title('Scatter plot')
        plt.xlabel('\u03B3')
        plt.ylabel('\u03B1')
        plt.savefig(img_name)

    def output(self):
        create_dir(RESULT_DIR)
        self.__save_to_csv()
        self.__save_to_img()