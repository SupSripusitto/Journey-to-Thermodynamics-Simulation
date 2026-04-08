import numpy as np
import matplotlib.pyplot as plt

n = 5 # Number of molecules
dt = 0.01 # Step size

v = np.random.rand(2,n)-0.5
x = np.random.rand(2,n)

for i in range(100):
    x += v*dt
    plt.clf()
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.scatter(x[0,:],x[1,:])
    plt.pause(0.00001)

plt.show()