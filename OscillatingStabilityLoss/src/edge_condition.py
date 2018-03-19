from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import cmath
from numba import jit

@jit(nopython=True, nogil = True, target='cpu')
def func(F, omegas, alphas):
	for i in range(F.shape[0]):
		for j in range(F.shape[1]):
			mu = cmath.sqrt(complex(-gamma, omegas[j]))
			F[i, j] = abs(mu * cmath.sinh(mu) - alphas[i] * cmath.cosh(mu * shift))

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data
shift = 0.0
gamma = 2.0

alphas = np.linspace(-2.5, 2.5, 2001)
omegas = np.linspace(-2.5, 2.5, 2001)
F = np.zeros((len(alphas), len(omegas)))
func(F, omegas, alphas)
print(F.min(), F.argmin())

#ax.plot_surface(alphas, omegas, F)

#plt.show()

