import numpy as np
import matplotlib.pyplot as plt

n = 100 # Number of molecules
dt = 0.001 # Step size (time in second)

xrange = 1
yrange = 1 # Define the box size (in meter)

v_rms = 10 # Average velocity (in m/s)

v = np.random.normal(v_rms/np.sqrt(2),1,size=(2,n))
x = np.random.normal(0,1,size=(2,n))
x[0,:] = x[0,:]*xrange
x[1,:] = x[1,:]*yrange

plt.style.use('dark_background')

for i in range(1000):
    x += v*dt

    # Consider x-position
    x0 = x[0,:]
    v0 = v[0,:]
    
    # Index the BC
    xl = x0 < 0
    xu = x0 > xrange
    # Calculate collision
    v0[xl] = -v0[xl]
    x0[xl] = -x0[xl]

    v0[xu] = -v0[xu]
    x0[xu] = -x0[xu]+2*xrange

    # Consider y-position
    x1 = x[1,:]
    v1 = v[1,:]
    
    # Index the BC
    yl = x1 < 0
    yu = x1 > yrange
    # Calculate collision
    v1[yl] = -v1[yl]
    x1[yl] = -x1[yl]

    v1[yu] = -v1[yu]
    x1[yu] = -x1[yu]+2*yrange
    
    # Update bouncing position
    x[0,:] = x0
    v[0,:] = v0
    x[1,:] = x1
    v[1,:] = v1

    plt.clf()
    plt.xlim(0,xrange)
    plt.ylim(0,yrange)
    plt.scatter(x[0,:],x[1,:],c='lime',s=5)
    plt.pause(0.0001)

# Root Mean Square velocity to indicate accuracy of temperature
# print(np.sqrt((np.dot(v0,v0)+np.dot(v1,v1))/n))

plt.show()