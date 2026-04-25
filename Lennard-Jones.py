import numpy as np
import matplotlib.pyplot as plt

n = 2 # Number of molecules (Recommended minimum number = 550)
t = 0.01 # Time interval in second
timepoint = 10000 # Number of snapshots
dt = t/timepoint # Recommended to has dt at most at 0.1 and t at least 50

epsilon = 1e-10
sigma = 1e-10

xrange = 5
yrange = 5 # Define the box size in angstrom

xrange /= 1e10
yrange /= 1e10

# Define temperature
T = 0 # in Kelvin

# Assume m = 1, calculate the velocity rms
v_rms = np.sqrt(2*T*1.380649e-23) # Average velocity (in m/s)

v = np.random.normal(0,v_rms/np.sqrt(2),size=(2,n))
r = np.random.random((2,n))

r[0,:] = r[0,:]*xrange
r[1,:] = r[1,:]*yrange

x = r[0,:]
y = r[1,:]

vx = v[0,:]
vy = v[1,:]

def acceleration(x,y):
    x = x.reshape((1,n))
    y = y.reshape((1,n))

    dx = x - x.T
    dy = y - y.T

    rsq = dx**2 + dy**2
    np.fill_diagonal(rsq,np.inf) # Prevent zero division

    f = 24*epsilon*(2*sigma**12/rsq**7-sigma**6/rsq**4)
    ax = np.sum(f*dx,axis=0)
    ay = np.sum(f*dy,axis=0)

    return (ax,ay)

ax, ay = acceleration(x,y)

TotImpulse = 0 # Impulse from wall collisions counter

plt.style.use('dark_background')

for i in range(timepoint):
    vx += dt/2*ax
    vy += dt/2*ay

    x += dt*vx
    y += dt*vy

    ax, ay = acceleration(x,y)

    vx += dt/2*ax
    vy += dt/2*ay

    # Index the BC
    xl = x < 0
    xu = x > xrange

    # Calculate collision
    vx[xl] = -vx[xl]
    x[xl] = -x[xl]

    vx[xu] = -vx[xu]
    x[xu] = -x[xu]+2*xrange
    
    # Index the BC
    yl = y < 0
    yu = y > yrange

    # Calculate collision
    vy[yl] = -vy[yl]
    y[yl] = -y[yl]

    vy[yu] = -vy[yu]
    y[yu] = -y[yu]+2*yrange

    plt.clf()
    plt.xlim(0,xrange)
    plt.ylim(0,yrange)
    plt.scatter(x,y,c='lime',s=5)
    plt.pause(1/timepoint)

    # Calculating impulse done by gas in this snapshot
    TotImpulse += 2*(np.sum(np.abs(vx[xl])) + np.sum(np.abs(vx[xu])))
    TotImpulse += 2*(np.sum(np.abs(vy[yl])) + np.sum(np.abs(vy[yu])))

# Root Mean Square velocity to indicate accuracy of temperature
print('v_rms =', np.sqrt((np.dot(vx,vx)+np.dot(vy,vy))/n))

print('T =', (np.dot(vx,vx)+np.dot(vy,vy))/n/2/1.380649e-23)
print('P =', TotImpulse*.5/(xrange+yrange)/t)