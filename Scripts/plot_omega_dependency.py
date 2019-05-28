import pandas as pd
import matplotlib.pyplot as plt
import os


DATA_PATH = 'C:/_Repositories/KaschenkoEquation/Tracer/Results/x0=0.00'
CSV_FILE = 'x0=0.00_analytical.csv'
DIR_PICS = '../Tracer/Results/Omegas'
PICT_NAME = 'omegas_x0=0.00.png'


df = pd.read_csv(os.path.join(DATA_PATH, CSV_FILE), sep=';')
gs = list(df['gamma'])
ws = list(df['w'])
plt.rcParams.update({'font.size': 13})
plt.subplots_adjust(left=0.11, bottom=0.11, right=0.98, top=0.98)
plt.xlabel('$\gamma$')
plt.ylabel('$\omega$', rotation='horizontal', position=(0.0,0.55))
plt.grid()
plt.plot(gs, ws, color='g', linewidth=2)
plt.savefig(os.path.join(DIR_PICS, PICT_NAME))