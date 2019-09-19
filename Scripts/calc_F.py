import pandas as pd
import cmath


def F(a, g, l, x0):
    mu = cmath.sqrt(-g+l)
    return mu*cmath.sinh(mu) - a*cmath.cosh(mu*x0)


def F_der(a, g, l, x0):
    mu = cmath.sqrt(-g+l)
    return (cmath.sinh(mu) + mu*cmath.cosh(mu) - a*x0*cmath.sinh(mu*x0)) / (2.0*mu)

def F_derder(a, g, l, x0):
    mu = cmath.sqrt(-g + l)
    first = 0.25*(cmath.cosh(mu)/(mu*mu) - cmath.sinh(mu)/(mu*mu*mu))
    second = cmath.sinh(mu)/(4.0*mu)
    third = -((a*x0)/4.0)*((x0*cmath.cosh(mu*x0))/(mu*mu) - (cmath.sinh(mu*x0))/(mu*mu*mu))
    return first+second+third


x0 = 0.49
g = 14.738
l = 8.05513j
a = -9.08828
f = F(a, g, l, x0)
fd = F_der(a, g, l, x0)
#fdd = F_derder(a, g, l, x0)
print('F={}'.format(f))
print('F\'={}'.format(fd))
#print('F\'\'(0)={:.4}'.format(fdd))