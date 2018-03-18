import numpy as np
import matplotlib.pyplot as mpt


p=np.pi
x=np.linspace(0,2*p,401)
x=x[:-1]        #removing the last element for
                #a proper periodic integral

def f1(t):
    return np.exp(t)

def f2(t):
    return np.cos(np.cos(t))

b1=f1(x)          #vector with exp(x) values
b2=f2(x)          #vector with cos(cos(x))
mat=np.zeros([400,51]) #the matrix for the operation
mat[:,0] = 1    #First column is 1
ran=range(1,mat.shape[1])
odd_ind = ran[0::2]
even_ind = ran[1::2]
multi_count=1       #analogous to k in cos(or sin)(kx)

for even_col_no,odd_col_no in zip(even_ind,odd_ind):
   mat[:,odd_col_no] = np.cos(multi_count*x)
   mat[:,even_col_no] = np.sin(multi_count*x)

   multi_count+=1

cl_exp=np.linalg.lstsq(mat,b1,rcond=-1)[0]
cl_cs2=np.linalg.lstsq(mat,b2,rcond=-1)[0]
print('The coefficients for exp(x) and cos(cos(x)) are-')
print(cl_exp,cl_cs2)

a_l1=list()             #a for cos(cos))
b_l1=list()             #b for cos(cos))
a_l2=list()             #a for exp
b_l2=list()             #b for exp
b_l1.append(0)          #0 is the first element for b
b_l2.append(0)          #b0=0
a_l1.append(cl_cs2[0])  #a0 appended to a_list
a_l2.append(cl_exp[0])  #a0 appended to a list
a_temp1=cl_cs2[1::2]    #a is at odd indices
b_temp1=cl_cs2[2::2]    #b at the even indices except 0
a_temp2=cl_exp[1::2]
b_temp2=cl_exp[2::2]

for a1,b1,a2,b2 in zip(a_temp1,b_temp1,a_temp2,b_temp2):
    a_l1.append(a1)     #a for cs2
    b_l1.append(b1)
    a_l2.append(a2)     #a for exp
    b_l2.append(b2)

ra=range(0,26)
a_l1=list(map(abs,a_l1))
b_l1=list(map(abs,b_l1))
a_l2=list(map(abs,a_l2))
b_l2=list(map(abs,b_l2))

mpt.figure(7)
mpt.title('For cos(cos(x))')
mpt.loglog(ra,a_l1,'go',ra,b_l1,'ro')
mpt.xlabel('n')
mpt.ylabel('approx. fourier coefficients')
mpt.legend('ab')

mpt.figure(8)
mpt.title('For exp(x)')
mpt.loglog(ra,a_l2,'go',ra,b_l2,'ro')
mpt.xlabel('n')
mpt.ylabel('approx. fourier coefficients')
mpt.legend('ab')
mpt.show()
