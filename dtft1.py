import numpy as np
from matplotlib import pyplot as plt
j=(-1)**(0.5)
w=np.arange(-1*np.pi,np.pi,0.01*np.pi)
m=np.arange(0,500)
F=250
fs=10000
s1=2*np.cos(2*np.pi*(F)*m+np.pi/2);
s=2*np.cos(2*np.pi*(F/fs)*m+np.pi/2);
x=[]
for i in range(0,len(w)):
		sum=0
		for n in range(0,len(s)):
				sum=sum+s[n]*np.exp(-1*j*w[i]*n)
		x.append(sum)
plt.subplot(2,2,1)
plt.plot(m,s1)
plt.subplot(2,2,2)
plt.plot(m,s)
plt.subplot(2,2,3)
plt.plot(w,np.abs(x))
plt.subplot(2,2,4)
plt.plot(w,np.angle(x))
plt.show();


