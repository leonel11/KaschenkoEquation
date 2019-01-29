import pandas as pd
import numpy as np
import cmath

DATA_FILE = '../Tracer/Results/x0=0.00_.csv'
x0 = 0.0
c = 1.0

def getMu(g, w):
    return cmath.sqrt(complex(-g, w))

def getQ1(mu):
    return cmath.sinh(3.0*mu+np.conj(mu)) + cmath.sinh(3.0*mu-np.conj(mu)) + \
           cmath.sinh(mu+np.conj(mu)) + cmath.sinh(mu-np.conj(mu))

def getQ2(mu):
    return cmath.cosh(3.0*mu+np.conj(mu)) + cmath.cosh(3.0*mu-np.conj(mu)) + \
           3.0*cmath.cosh(mu+np.conj(mu)) + 3.0*cmath.cosh(mu-np.conj(mu))

def getF1(mu, y):
    C = getC(mu)
    return cmath.cosh((3.0*mu+np.conj(mu))*y)/(3.0*mu+np.conj(mu)) + \
           cmath.cosh((3.0*mu-np.conj(mu))*y)/(3.0*mu-np.conj(mu)) + \
           cmath.cosh((mu+np.conj(mu))*y)/(mu+np.conj(mu)) + cmath.cosh((mu-np.conj(mu))*y)/(mu-np.conj(mu)) - C

def getF2(mu, y):
    return cmath.sinh((3.0*mu+np.conj(mu))*y)/(3.0*mu+np.conj(mu)) + \
           cmath.sinh((3.0*mu-np.conj(mu))*y)/(3.0*mu-np.conj(mu)) + \
           3.0*cmath.sinh((mu+np.conj(mu))*y)/(mu+np.conj(mu)) + 3.0*cmath.sinh((mu-np.conj(mu))*y)/(mu-np.conj(mu))

def getA(mu, alpha, x0):
    return (2*mu*(mu*cmath.cosh(mu)-cmath.sinh(mu)) + \
           alpha*cmath.sinh(mu*x0)*(cmath.sinh(2.0*mu*x0)-cmath.cosh(2.0*mu*x0)-2.0*mu*x0)) / (4.0*mu*mu)

def getPhi(mu, alpha, x0):
    A = getA(mu, alpha, x0)
    return c*cmath.cosh(mu*x0)/A

def getC(mu):
    return 1.0/(3.0*mu+np.conj(mu)) + 1.0/(3.0*mu-np.conj(mu)) + 1.0/(mu+np.conj(mu)) + 1.0/(mu-np.conj(mu))

def getB(mu, alpha, x0):
    Q1 = getQ1(mu)
    Q2 = getQ2(mu)
    F1_1 = getF1(mu, 1.0)
    F2_1 = getF2(mu, 1.0)
    F1_x0 = getF1(mu, x0)
    F2_x0 = getF2(mu, x0)
    return (3.0*c**3)/(8.0*mu) * (alpha*(cmath.sinh(mu*x0)*F1_x0-cmath.cosh(mu*x0)*F2_x0) + \
           (Q1*cmath.cosh(mu) - Q2*cmath.sinh(mu)) + mu*(cmath.sinh(mu)*F2_1-cmath.cosh(mu)*F1_1))

def getD(mu, alpha, x0):
    B = getB(mu, alpha, x0)
    A = getA(mu, alpha, x0)
    return B/A

def main():
    crit = pd.read_csv(DATA_FILE, sep = ';')
    ReD = []
    RePhi = []
    for i in range(len(crit)):
        g, a, w = crit.index[i], crit['a'][i], crit['w'][i]
        mu = getMu(g, w)
        phi = getPhi(mu, a, x0)
        d = getD(mu, a, x0)
        RePhi.append(float('{:.3}'.format(phi.real)))
        ReD.append(float('{:.3}'.format(d.real)))
    crit['red'] = ReD
    crit['rephi'] = RePhi
    crit.to_csv(DATA_FILE, index=False)
    pass

if __name__ == '__main__':
    main()
