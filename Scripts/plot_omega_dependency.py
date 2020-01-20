'''
Script for visualization omega values (imaginary part of purely imaginary
eigenvalues) for fixed x0 when zero solution of LINEARIZED BOUNDARY-VALUE PROBLEM
loses its stability in OSCILLATING way
'''

import pandas as pd
import os
import drawer


x0 = 0.41
AFTER_TANGENT = True

SUFFIX_NAME = '_after_tangent' if AFTER_TANGENT else ''
DATA_PATH = '../Tracer/Results' + f'/x0={x0:.2f}'
CSV_FILE = DATA_PATH + f'/x0={x0:.2f}' + '_analytical.csv'
AFTER_TANGENT_FILE = DATA_PATH + f'/x0={x0:.2f}' + '_analytical_after_tangent.csv'
SAVE_DIRECTORY = '../Tracer/Results/Omegas'
PICT_NAME = SAVE_DIRECTORY + f'/omegas_x0={x0:.2f}' + SUFFIX_NAME + '.png'


def read_params():
    '''
    Read params for visualization
    :return list of gamma values, list of omega values
    '''
    gs, ws = [], []
    if AFTER_TANGENT:
        if os.path.exists(AFTER_TANGENT_FILE):
            df = pd.read_csv(AFTER_TANGENT_FILE, sep=';')
            gs, ws = list(df['gamma']), list(df['w'])
    else:
        df = pd.read_csv(CSV_FILE, sep=';')
        gs, ws = list(df['gamma']), list(df['w'])
    return gs, ws


if __name__ == '__main__':
    gs, ws = read_params()
    # draw omega dependency
    drawer_w = drawer.Drawer(x_label=r'$\gamma$', y_label=r'$\omega$',
                             save_dir=SAVE_DIRECTORY)
    drawer_w.drawCurve(gs, ws, curve_color='g', save_name=PICT_NAME)