import matplotlib.pyplot as plt
import numpy as np
import pylab

F=-0.7296
[Es,Dsup,Dsdwn]=np.loadtxt('S_s_pdos',unpack=True,usecols=(0,1,2))
#[Ep,Dpup,Dpdwn]=np.loadtxt('N_p.dat',unpack=True)
#[Ep,Dpup,Dpdwn]=np.loadtxt('N_p.dat',unpack=True)


plt.plot(Es-F,Dsup,label='S(s)_up')
plt.plot(Es-F,-Dsdwn,label='S(s)_down')
#pylab.xlim([-5,13])
#plt.plot(D,E-F,label='S(total)')
plt.axvline(x=0,color='red',linestyle=':')
plt.ylabel('PDOS')
plt.xlabel('E-E$_f$')
plt.title('1D NbS2')
plt.legend()
plt.show()
