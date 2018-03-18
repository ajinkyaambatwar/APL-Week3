import numpy as np
import four
import lsa

a_f1_lsa=np.asarray(lsa.a_l1)       #for cs2
a_f2_lsa=np.asarray(lsa.a_l2)       #for exp(x)
b_f1_lsa=np.asarray(lsa.b_l1)       #for cs2
b_f2_lsa=np.asarray(lsa.b_l2)       #for exp(x)
a_f1_quad=np.asarray(four.a_f2)     #for cs2
a_f2_quad=np.asarray(four.a_f1)     #for exp(x)
b_f1_quad=np.asarray(four.b_f2)     #for
b_f2_quad=np.asarray(four.b_f1)
b_f1_lsa=np.delete(b_f1_lsa,0)      #first element is zero which is not needed
b_f2_lsa=np.delete(b_f2_lsa,0)
b_f1_quad=np.delete(b_f1_quad,0)
b_f2_quad=np.delete(b_f2_quad,0)
a_f1_err=a_f1_lsa-a_f1_quad
a_f2_err=a_f2_lsa-a_f2_quad
b_f1_err=b_f1_lsa-b_f1_quad
b_f2_err=b_f2_lsa-b_f2_quad
a_f1_err_max=abs(np.amax(a_f1_err))
a_f2_err_max=abs(np.amax(a_f2_err))
b_f1_err_max=abs(np.amax(b_f1_err))
b_f2_err_max=abs(np.amax(b_f2_err))

print('The largest deviation in a for cos(cos(x)), a for exp(x), b for cos(cos(x)), b for exp(x) ')
print(a_f1_err_max, a_f2_err_max, b_f1_err_max, b_f2_err_max)
