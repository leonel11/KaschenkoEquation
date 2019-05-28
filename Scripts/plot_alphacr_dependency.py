import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


x0 = 0.67
DATA_PATH = 'C:/_Repositories/KaschenkoEquation/Tracer/Results/x0=0.67'
CSV_FILE = 'x0=0.67_analytical.csv'


def get_alpha_u(g, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        return mu*np.sinh(mu)/np.cosh(mu*x0)
    else:
        mu = np.sqrt(g)
        return -mu*np.sin(mu)/np.cos(mu*x0)


def visualise_alphas(gs, aus, acs):
    plt.rcParams.update({'font.size': 13})
    plt.subplots_adjust(left=0.11, bottom=0.11, right=0.98, top=0.98)
    plt.xlabel('$\gamma$')
    plt.ylabel(r'$\alpha_{cr}$', rotation='horizontal', position=(0.0, 0.55))
    plt.grid()
    plt.plot(gs, aus, label=r'$\alpha_u$', color='b', linewidth=2, zorder=3)
    plt.plot(gs, acs, label=r'$\alpha_c$', color='red', linewidth=2, zorder=3)
    plt.legend(loc='lower right')
    plt.scatter(gs[0], acs[0], color='black', s=12, zorder=4)
    plt.axhline(y=0.0, linewidth=2, color='grey', zorder=2)
    plt.axvline(x=0.0, linewidth=2, color='grey', zorder=2)
    #x1,x2,y1,y2 = plt.axis()
    #plt.axis((-0.65,4.4,-21.5,4))
    plt.savefig(os.path.join(DATA_PATH, 'alphas.png'))


df = pd.read_csv(os.path.join(DATA_PATH, CSV_FILE), sep=';')
gammas = list(df['gamma'])
alpha_c = list(df['alpha_c'])
alpha_u = [get_alpha_u(g, x0) for g in gammas]
print('right(alpha_u) = {:.5}'.format(alpha_u[0]))
print('min(alpha_u) = {:.5}'.format(min(alpha_u)))
visualise_alphas(gammas, alpha_u, alpha_c)