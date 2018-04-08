from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import cmath
from numba import jit

@jit(nopython=True, nogil = True, target='cpu')
def func(F, omegas, alphas):
	for i in range(F.shape[0]):
		for j in range(F.shape[1]):
			mu = cmath.sqrt(complex(-gamma, omegas[i, j]))
			F[i, j] = abs(mu * cmath.sinh(mu) - alphas[i, j] * cmath.cosh(mu * shift))
			#F[i, j] = (mu * cmath.sinh(mu) - alphas[i, j] * cmath.cosh(mu) * cmath.exp(complex(0, omegas[i, j] * shift))).real	

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlabel('\u03B1')
ax.set_ylabel('\u03C9')
ax.set_zlabel('F')

# Make data
shift = 0.0
gamma = 0.5

alphas = np.linspace(-75.0, 75.0, 3701)
omegas = np.linspace(-75.0, 75.0, 3701)
alphas, omegas = np.meshgrid(alphas, omegas)
F = np.zeros(alphas.shape)
func(F, omegas, alphas)
print(F.min(), F.argmin())

ax.plot_surface(alphas, omegas, F)

plt.show()

