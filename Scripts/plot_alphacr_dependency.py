import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


x0 = 0.41
DATA_PATH = 'C:/_Repositories/KaschenkoEquation/Tracer/Results/x0=0.41'
CSV_FILE = 'x0=0.41_analytical.csv'
AFTER_TANGENT = True
AFTER_TANGENT_FILE = 'x0=0.41_analytical_after_tangent.csv'


def get_alpha_u(g, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        return mu*np.sinh(mu)/np.cosh(mu*x0)
    else:
        mu = np.sqrt(g)
        return -mu*np.sin(mu)/np.cos(mu*x0)


def visualise_alphas(gs, aus, acs, gfs, afs):
    plt.rcParams.update({'font.size': 13})
    plt.subplots_adjust(left=0.13, bottom=0.11, right=0.98, top=0.98)
    plt.xlabel('$\gamma$')
    plt.ylabel(r'$\alpha_{cr}$', rotation='horizontal', position=(0.0, 0.55))
    plt.grid()
    plt.plot(gs, aus, label=r'$\alpha_u$', color='b', linewidth=2, zorder=4)
    if AFTER_TANGENT:
        plt.plot(gfs, afs, label=r'$\alpha_f$', color='olive', linewidth=2, zorder=3)
    plt.plot(gs, acs, label=r'$\alpha_c$', color='red', linewidth=2, zorder=4)
    plt.legend(loc='lower right')
    plt.scatter(gs[0], acs[0], color='black', s=12, zorder=5)
    plt.axhline(y=0.0, linewidth=2, color='grey', zorder=2)
    plt.axvline(x=0.0, linewidth=2, color='grey', zorder=2)
    x1,x2,y1,y2 = plt.axis()
    plt.axis((x1,x2,-100,10))
    plt.savefig(os.path.join(DATA_PATH, 'alphas.png'))
    #plt.show()


df = pd.read_csv(os.path.join(DATA_PATH, CSV_FILE), sep=';')
gammas = list(df['gamma'])
alpha_c = list(df['alpha_c'])
if AFTER_TANGENT:
    df_f = pd.read_csv(os.path.join(DATA_PATH, AFTER_TANGENT_FILE), sep=';')
    gammas_f = list(df_f['gamma'])
    alphas_f = list(df_f['alpha_f'])
else:
    gammas_f, alphas_f = [], []
alpha_u = [get_alpha_u(g, x0) for g in gammas]
print('right(alpha_u) = {:.5}'.format(alpha_u[0]))
print('min(alpha_u) = {:.5}'.format(min(alpha_u)))
visualise_alphas(gammas, alpha_u, alpha_c, gammas_f, alphas_f)
#visualise_alphas(gammas[:80], alpha_u[:80], alpha_c[:80], gammas_f, alphas_f)