import numpy as np
import matplotlib.pyplot as plt

n = 50000 # Number of molecules (Recommended minimum number = 550)
t = 50 # Time interval in second
timepoint = 1000 # Number of snapshots
dt = t/timepoint # Recommended to has dt at most at 0.1 and t at least 50

xrange = 10
yrange = 10 # Define the box size in angstrom

xrange /= 1e10
yrange /= 1e10

# Define temperature
T = 340 # in Kelvin

# Assume m = 1, calculate the velocity rms
v_rms = np.sqrt(2*T*1.380649e-23) # Average velocity (in m/s)

v = np.random.normal(0,v_rms/np.sqrt(2),size=(2,n))
x = np.random.random((2,n))

x[0,:] = x[0,:]*xrange
x[1,:] = x[1,:]*yrange

TotImpulse = 0 # Impulse from wall collisions counter

plt.style.use('dark_background')

for i in range(timepoint):
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
    plt.pause(1/timepoint)

    # Calculating impulse done by gas in this snapshot
    TotImpulse += 2*(np.sum(np.abs(v0[xl])) + np.sum(np.abs(v0[xu])))
    TotImpulse += 2*(np.sum(np.abs(v1[yl])) + np.sum(np.abs(v1[yu])))

# Root Mean Square velocity to indicate accuracy of temperature
print('v_rms =', np.sqrt((np.dot(v0,v0)+np.dot(v1,v1))/n))

print('T =', (np.dot(v0,v0)+np.dot(v1,v1))/n/2/1.380649e-23)
print('P =', TotImpulse*.5/(xrange+yrange)/t)