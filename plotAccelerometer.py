# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 04:03:14 2023

@author: Davis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
df = pd.read_csv("puzzle1.csv")
samplingRate = 30

# extract accelerations
accelx =df.loc[2*samplingRate:4.3*samplingRate,"accelerometerAccelerationX"]
accely = df.loc[2*samplingRate:4.3*samplingRate:,"accelerometerAccelerationY"]
accelx = accelx.values
accely = accely.values

# flip and center on mean
accelx = -accelx + np.mean(accelx)
accely = -accely + np.mean(accely)

# generate time vector
numTimes = len(accelx)
t = np.linspace(0, (numTimes-1)/samplingRate,numTimes)

#plot acceleration
f, axes = plt.subplots(4,1)

axes[0].plot(t,accelx,'o-',t,accely,'o-')
axes[3].set_xlabel('time (sec)')
axes[0].set_ylabel('acceleration')
axes[0].legend(['x','y'])

#DO NOT CHANGE ABOVE THIS LINE

#%%
# b.)calculate jerk using centered divided difference function
from centeredDividedDifference import centeredDividedDifference
jerkx = centeredDividedDifference(accelx,1/samplingRate)
jerky = centeredDividedDifference(accely,1/samplingRate)

axes[1].plot(t[2:],jerkx,'o-',t[2:],jerky,'o-')
axes[1].set_ylabel('Jerk')
axes[1].legend(['x','y'])

#%% c.)Compute the x and y components of velocity (velx, vely) usingcumtrapz
velx = integrate.cumtrapz(accelx,t,initial = 0)
vely = integrate.cumtrapz(accely,t,initial = 0)

axes[2].plot(t,velx,'o-',t,vely,'o-')
axes[2].set_ylabel('Velocity')
axes[2].legend(['x','y'])
#%% d.)Compute the x and y components of position (posx, posy) using cumtrapz
posx = integrate.cumtrapz(velx,t,initial=0)
posy = integrate.cumtrapz(vely,t,initial=0)

axes[3].plot(t,posx,'o-',t,posy,'o-')
axes[3].set_ylabel('Position')
axes[3].legend(['x','y'])
plt.show()

#e.) The letter is V
#Plot of x-position vs. y-position
plt.figure(figsize=(10, 6   ))
plt.scatter(posx, posy, marker='o')
plt.ylabel('Y Position')
plt.xlabel('X Position')
plt.title('X Position vs. Y Position')
plt.grid(True)
plt.show()