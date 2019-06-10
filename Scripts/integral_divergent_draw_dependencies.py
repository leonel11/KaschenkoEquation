import numpy as np
import matplotlib.pyplot as plt


g_min = -4.0
g_max = 1000.0
h = 0.001


plt.rcParams.update({'font.size': 13})
plt.rcParams['savefig.directory'] = '../Tracer/Variations/Integral Boundary Condition'


def d_func(g):
    if g < 0:
        return -5.0*g*np.sinh(3.0*np.sqrt(-g))/(48.0*np.sinh(np.sqrt(-g))) - 0.75
    else:
        return -5.0*g*np.sin(3.0*np.sqrt(g))/(48.0*np.sin(np.sqrt(g))) - 0.75


def print_sign_points(gammas, ds):
    for idx in range(len(ds)-1):
        if ds[idx]*ds[idx+1] < 0:
            print(np.mean([gammas[idx], gammas[idx+1]]))


def prepare_plot():
    plt.xlabel('$\gamma$')
    plt.grid(True)
    plt.subplots_adjust(left=0.08, bottom=0.11, right=0.98, top=0.98)
    plt.axhline(y=0.0, linewidth=2, color='grey', zorder=2)


def draw_phid_dependencies(gammas, ds):
    plt.figure('integral_divergent_d0_g[{:.5},{:.5}]'.format(g_min, g_max))
    prepare_plot()
    plt.ylabel('$d_0$', rotation='horizontal', position=(0.0, 0.55))
    plt.plot(gammas, ds, color='darkorange', linewidth=2, zorder=3)
    # x1,x2,y1,y2 = plt.axis()
    # plt.axis((x1,4.902,y1,y2))
    plt.show()


def draw_amplitude_dependency(gammas, amps):
    plt.figure('divergent_A_g[{:.5},{:.5}]'.format(g_min, g_max))
    prepare_plot()
    plt.ylabel('$A$', rotation='horizontal', position=(0.0, 0.55))
    plt.plot(gammas, amps, label='$A_u$', color='crimson', linewidth=2)
    plt.legend()
    plt.show()


gammas = list(np.arange(g_min, g_max, h))
ds = [d_func(g) for g in gammas]
amps = [np.sqrt(1.0/abs(d)) for d in ds]
print_sign_points(gammas, ds)
draw_phid_dependencies(gammas, ds)
draw_amplitude_dependency(gammas, amps)