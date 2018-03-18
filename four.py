import numpy as np
import matplotlib.pyplot as mpt
from scipy.integrate import quad

def f1(x):
    return np.exp(x)

def f2(x):
    return np.cos(np.cos(x))

def u(t,f,k):
    return f(t)*np.cos(k*t)            #u for cos

def v(t,f,k):
    return f(t)*np.sin(k*t)            #v for sin

p=np.pi
vec=range(1,26)

a_f1=list()
b_f1=list()
a_f2=list()
b_f2=list()

a0=quad(f1,0,2*p)[0]
a0=a0/(2*p)
a0_2=quad(f2,0,2*p)[0]
a0_2=a0_2/(2*p)
a_f1.append(a0)             #a for exp(x)
a_f2.append(a0_2)           #a for cos(cos(X))
b_f1.append(0)              #b for exp(x)
b_f2.append(0)              #b for cos(cos(x))

for i in vec:
    a_temp1 = quad(u,0,2*p,args=(f1,i))[0]
    a_temp1 = a_temp1/p
    a_temp2 = quad(u,0,2*p,args=(f2,i))[0]
    a_temp2 = a_temp2/p
    a_f1.append(a_temp1)    #a for exp
    a_f2.append(a_temp2)    #a for cs2
    b_temp1 = quad(v,0,2*p,args=(f1,i))[0]
    b_temp1 = b_temp1/p
    b_temp2 = quad(v,0,2*p,args=(f2,i))[0]
    b_temp2 = b_temp2/p
    b_f1.append(b_temp1)
    b_f2.append(b_temp2)

#print(a_f1)
vec=range(0,26)
final_list1=list()
final_list2=list()


for a_t,b_t,a2_t,b2_t in zip(a_f1,b_f1,a_f2,b_f2):
    lit = [a_t,b_t]
    lit2 = [a2_t,b2_t]
    final_list1.append(lit)
    final_list2.append(lit2)

final_listar=np.asarray(final_list1)
final_list_2ar=np.asarray(final_list2)
outp1=final_listar.flatten()
outp1=np.delete(outp1,1)
outp2=final_list_2ar.flatten()
outp2=np.delete(outp2,1)

print('The vector for exp(x) is')
print(outp1)
print('The vector for cos(cos(x)) is')
print(outp2)

b_f1=list(abs(i) for i in b_f1)
b_f2=list(abs(k) for k in b_f2)
#---------plotting--------
#---------e^x------------
mpt.figure(3)       #for log-log plots
mpt.title('Coefficients for $e^{x}$(log scale)')
mpt.plot(vec,a_f1,'bo',vec,b_f1,'ro')
mpt.yscale('log')
mpt.xscale('log')
mpt.xlabel('n')
mpt.legend('ab')
mpt.ylabel('fourier coefficients')

mpt.figure(4)       #for semilogy
mpt.title('coefficients for $e^{x}$(semilog scale)')
mpt.plot(vec,a_f1,'bo',vec,b_f1,'ro')
mpt.yscale('log')
mpt.xlabel('n')
mpt.legend('ab')
mpt.ylabel('fourier coefficents')

#---------cos(cos(x))---------
mpt.figure(5)
mpt.title('coefficients for cos(cos(x))(log scale)')
mpt.plot(vec,a_f2,'bo',vec,b_f2,'ro')
mpt.yscale('log')
mpt.xscale('log')
mpt.xlabel('n')
mpt.legend('ab')
mpt.ylabel('fourier coefficents')

mpt.figure(6)
mpt.title('Coefficients for cos(cos(x))(semilog scale)')
mpt.plot(vec,a_f2,'bo',vec,b_f2,'ro')
mpt.yscale('log')
mpt.xlabel('n')
mpt.legend('ab')
mpt.ylabel('fourier coefficents')
mpt.show()
