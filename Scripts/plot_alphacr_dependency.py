import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


x0 = 0.25
DATA_PATH = 'C:/_Repositories/KaschenkoEquation/Tracer/Results/x0=0.25 (u13)'
CSV_FILE = 'x0=0.25_analytical.csv'


def get_alpha_u(g, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        return mu*np.sinh(mu)/np.cosh(mu*x0)
    else:
        mu = np.sqrt(g)
        return -mu*np.sin(mu)/np.cos(mu*x0)


def visualise_alphas(gs, aus, acs):
    plt.rcParams.update({'font.size': 13})
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.98, top=0.98)
    plt.xlabel('$\gamma$')
    plt.grid()
    plt.plot(gs, aus, label=r'$\alpha_u$', color='b', linewidth=2)
    plt.plot(gs, acs, label=r'$\alpha_c$', color='red', linewidth=2)
    plt.legend()
    plt.savefig(os.path.join(DATA_PATH, 'alphas.png'))


df = pd.read_csv(os.path.join(DATA_PATH, CSV_FILE), sep=';')
gammas = list(df['gamma'])
alpha_c = list(df['alpha_c'])
alpha_u = [get_alpha_u(g, x0) for g in gammas]
visualise_alphas(gammas, alpha_u, alpha_c)