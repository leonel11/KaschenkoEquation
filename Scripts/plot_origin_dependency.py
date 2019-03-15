import pandas as pd
import matplotlib.pyplot as plt
import os


DATA_PATH = 'C:/_Repositories/KaschenkoEquation/Tracer/Results/Origins'
CSV_FILE = 'origins_analytical.csv'
high_border = 0.88


df = pd.read_csv(os.path.join(DATA_PATH, CSV_FILE), sep=';')
gammas = list(df[df['x0'] < high_border]['x0'])
alphas = list(df[df['x0'] < high_border]['alpha'])
plt.rcParams.update({'font.size': 13})
plt.subplots_adjust(left=0.1, bottom=0.12, right=0.98, top=0.98)
plt.xlabel('$x_0$')
plt.grid()
plt.plot(gammas, alphas, label=r'$\alpha_c$', color='darkmagenta', linewidth=2)
plt.legend()
plt.savefig(os.path.join(DATA_PATH, 'origins.png'))