'''
Script for visualization alpha_c values (critical values of alpha, when
zero solution of LINEARIZED BOUNDARY-VALUE PROBLEM loses its stability
in OSCILLATING way) for different x0 values, from 0 to certain value of x0 -
x0_max
'''

import pandas as pd
import drawer


x0_max = 0.86

SAVE_DIRECTORY = '../Tracer/Results/Origins'
CSV_FILE = SAVE_DIRECTORY + '/origins_analytical.csv'
PICT_NAME = SAVE_DIRECTORY + f'/origins__x0_max={x0_max:.2f}' + '.png'


def read_params():
    '''
    Read params for visualization
    :return origins (list of gamma values, list of alpha_c (oscillating case) values)
    '''
    df = pd.read_csv(CSV_FILE, sep=';')
    gammas = list(df[df['x0'] <= x0_max]['x0'])
    alphas = list(df[df['x0'] <= x0_max]['alpha'])
    return gammas, alphas


if __name__ == '__main__':
    gammas, alphas = read_params()
    # draw origin dependency
    drawer_w = drawer.Drawer(x_label=r'$\gamma$', y_label=r'$\omega$',
                             save_dir=SAVE_DIRECTORY)
    drawer_w.drawCurve(gammas, alphas, curve_color='darkmagenta',
                       save_name=PICT_NAME)