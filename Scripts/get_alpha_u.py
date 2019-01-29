import numpy as np
import matplotlib.pyplot as plt


gamma = 4.9
x0 = 0.33


def alpha_u(gamma, x0):
    if gamma < 0:
        mu = np.sqrt(-gamma)
        return mu*np.sinh(mu)/np.cosh(mu*x0)
    else:
        mu = np.sqrt(gamma)
        return mu*np.sin(mu)/np.cos(mu*x0)


print('α = {:.6}'.format(alpha_u(gamma, x0)))