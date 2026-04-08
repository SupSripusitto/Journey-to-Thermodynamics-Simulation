import numpy as np
import matplotlib.pyplot as plt

n = 10 # Number of molecules
dt = 0.01 # Step size

xrange = 6 
yrange = 7 # Define the box size

v_rms = 10 # Average velocity

v = (np.random.rand(2,n)-0.5)*v_rms
x = np.random.rand(2,n)
x[0,:] = x[0,:]*xrange
x[1,:] = x[1,:]*yrange

for i in range(100):
    x += v*dt
    x[0,:] = x[0,:] % xrange
    x[1,:] = x[1,:] % yrange
    plt.clf()
    plt.xlim(0,xrange)
    plt.ylim(0,yrange)
    plt.scatter(x[0,:],x[1,:])
    plt.pause(0.0001)

plt.show()