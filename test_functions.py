from math import sqrt, pi
from numpy import sin, cos, exp, asarray

class BOHACHEVSKY:
    minimum = 0.0
    minima = (0, 0)
    x1_bounds = (-100, 100)
    x2_bounds = (-100, 100)

    def z(x, y):
        return x**2.0 + 2*(y**2.0) - 0.3*cos(3*pi*x) -0.4*cos(4*pi*y) + 0.7

    def df(x, y):
        return asarray([
            2*x + 0.9*pi*sin(3*pi*x),
            4*y + 1.6*pi*sin(4*pi*y)
        ])

class EASOM:
    minimum = -1
    minima = (pi, pi)
    x1_bounds = (-10, 10)
    x2_bounds = (-10, 10)

    def z(x, y):
        t1 = cos(x)
        t2 = cos(y)
        t3 = exp(-1*((x-pi)**2 + (y-pi)**2))
        return -1*t1*t2*t3

    def df(x, y):
        t2 = exp(-1*((x-pi)**2 + (y-pi)**2))
        return asarray([
            cos(y)*(cos(x)*t2*2*(x-pi) + t2*sin(x)),
            cos(x)*(cos(y)*t2*2*(y-pi) + t2*sin(y)),
        ])

#correct this
class MCCORMICK:
    minimum = -1
    minima = (pi, pi)
    x1_bounds = (-100, 100)
    x2_bounds = (-100, 100)

    def z(x, y):
        t1 = cos(x)
        t2 = cos(y)
        t3 = exp(-1*((x-pi)**2 + (y-pi)**2))
        return -1*t1*t2*t3

    def df(x, y):
        t2 = exp(-1*((x-pi)**2 + (y-pi)**2))
        return asarray([
            cos(y)*(cos(x)*t2*2*(x-pi) + t2*sin(x)),
            cos(x)*(cos(y)*t2*2*(y-pi) + t2*sin(y)),
        ])