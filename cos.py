import numpy as np
from matplotlib import pyplot as plt
n=np.arange(1,500,2)
F=250;
fs=10000;
f=F/fs;
s=0.5*np.cos(2*np.pi*f*n+np.pi/2)
plt.stem(n,s);plt.show();
