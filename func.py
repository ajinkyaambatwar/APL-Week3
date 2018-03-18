import numpy as np
import matplotlib.pyplot as mpt

def f1(x):
    return np.exp(x)

def f2(x):
    return np.cos(np.cos(x))

p=np.pi
vec = np.linspace(-2*p,4*p,1000)

#--------plotting---------
mpt.figure(1)
mpt.plot(vec,f1(vec))
mpt.yscale("log")
mpt.xlabel("x(linear scale)")
mpt.ylabel("$e^{x}$(log scale)")
mpt.grid(True)

mpt.figure(2)
mpt.plot(vec,f2(vec))
mpt.xlabel("x")
mpt.ylabel("cos(cos(x))")
mpt.grid(True)


mpt.show()
