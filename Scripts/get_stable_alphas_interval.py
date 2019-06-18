import numpy as np
import pandas as pd
import os


EPS = 0.01
x0 = 0.42
gamma = 5.7
DATA_PATH = 'C:/_Repositories/KaschenkoEquation/Tracer/Results/x0=0.42'
CSV_FILE = 'x0=0.42_analytical.csv'


def get_alpha_u(g, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        return mu*np.sinh(mu)/np.cosh(mu*x0)
    else:
        mu = np.sqrt(g)
        return -mu*np.sin(mu)/np.cos(mu*x0)


df = pd.read_csv(os.path.join(DATA_PATH, CSV_FILE), sep=';')
a_c = df['alpha_c'][(df['gamma'] < gamma+EPS) & (df['gamma'] > gamma-EPS)]
a_u = get_alpha_u(gamma, x0)
print('Stable: [{:.6}, {:.6}]'.format(a_c.values[0], a_u))