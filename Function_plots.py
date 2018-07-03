"""
@author: Paul Lyon


"""

import matplotlib.pyplot as plt
import numpy as np
from math import pi

START_TIME = 0.0
STOP_TIME = 2.0
TIME_STEP = 0.01
ARRAY_SIZE = int(STOP_TIME/TIME_STEP)
PLOT_SCALING = 1.5 #Scale y-axes to make plot look pretty
FIGURE_SIZE=(8,3)

#********************************
#Calculate Functions

time = np.arange(START_TIME, STOP_TIME, TIME_STEP)
Cosine_wave = np.cos(2*pi*time)
Sine_wave = np.sin(2*pi*time)
#Insert any other functions here to plot and reference
#in subplots
#*********************************

#Define plots and Display Results
plt.clf()
fig = plt.figure(1,figsize=(FIGURE_SIZE))
fig.set_facecolor('gray')
fig.frameon = True


#*****Subplot 1 ***********
ax1 = fig.add_subplot(121)  #Argument in add_subplot is x-y-position
ax1.plot(time, Cosine_wave) #Function on chart x-y plot
ax1.plot(time, Sine_wave)   #Second plot added to subplot 121 to show
                            # how it works


#Set axes 
ax1.set_xlim(START_TIME,STOP_TIME)
ax1.set_ylim(np.amin(Cosine_wave)*PLOT_SCALING, np.amax(Cosine_wave)*PLOT_SCALING)

#Add tiles and labels
ax1.set_title('Cosine Wave')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax1.grid(True) 

#*******Subplot 2********
ax2 = fig.add_subplot(122)
ax2.plot(time, Sine_wave)

ax2.set_xlim(START_TIME,STOP_TIME)
ax2.set_ylim((np.amin(Sine_wave)*PLOT_SCALING, np.amax(Sine_wave)*PLOT_SCALING))

ax2.set_title('Sine Wave')
ax2.set_xlabel('Time')
ax2.set_ylabel('Amplitude')
ax2.grid(True)

#************************

fig.tight_layout()

fig.show()