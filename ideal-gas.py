import numpy as np
import matplotlib.pyplot as plt

n = 30 # Number of molecules
dt = 0.001 # Step size

xrange = 6 
yrange = 7 # Define the box size

v_rms = 100 # Average velocity

v = (np.random.rand(2,n)-0.5)*v_rms
x = np.random.rand(2,n)
x[0,:] = x[0,:]*xrange
x[1,:] = x[1,:]*yrange

for i in range(100):
    x += v*dt

    # Consider x-position
    x0 = x[0,:]
    v0 = v[0,:]
    
    # Index the BC
    xl = x0 < 0
    xu = x0 > xrange
    # Calculate collision
    v0[xl] = -v0[xl]
    x0[xl] = -x0[xl]-v0[xl]*dt

    v0[xu] = -v0[xu]
    x0[xu] = -x0[xu]-v0[xu]*dt+2*xrange

    # Consider y-position
    x1 = x[1,:]
    v1 = v[1,:]
    
    # Index the BC
    yl = x1 < 0
    yu = x1 > yrange
    # Calculate collision
    v1[yl] = -v1[yl]
    x1[yl] = -x1[yl]-v1[yl]*dt

    v1[yu] = -v1[yu]
    x1[yu] = -x1[yu]-v1[yu]*dt+2*yrange
    
    # Update bouncing position
    x[0,:] = x0
    v[0,:] = v0
    x[1,:] = x1
    v[1,:] = v1

    plt.clf()
    plt.xlim(0,xrange)
    plt.ylim(0,yrange)
    plt.scatter(x[0,:],x[1,:])
    plt.pause(0.0001)

plt.show()