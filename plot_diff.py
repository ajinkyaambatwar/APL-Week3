import numpy as np
import matplotlib.pyplot as mpt
import lsa

c=lsa.cl_cs2
c_1=lsa.cl_exp
A=lsa.mat
p=np.pi
x=np.linspace(0,2*p,401)
x=x[:-1]
f_val=np.matmul(A,c)
f_val_exp=np.matmul(A,c_1)

mpt.figure(1)
mpt.plot(x,f_val,'go')
mpt.xlabel('x')
mpt.title('$cos(cos(x))$')
mpt.ylabel('$cos(cos(x))$')

mpt.figure(2)
mpt.plot(x,f_val_exp,'go')
mpt.xlabel('x')
mpt.ylabel('$e^x$')
mpt.title('$e^x$')
mpt.show()
