"""
@author: Paul Lyon

Simple script to plot functions with some simple formatting.

"""

import matplotlib.pyplot as plt
import numpy as np
from math import pi

START_TIME = 0.0
STOP_TIME = 2.0
TIME_STEP = 0.01
ARRAY_SIZE = int(STOP_TIME/TIME_STEP)

TITLE = 'Chart Showing Two functions'

AX1_TITLE = 'Cosine Wave'
AX1_XLABEL = 'Time'
AX1_YLABEL = 'Amplitude'

AX2_TITLE = 'Sine Wave'
AX2_XLABEL = 'Time'
AX2_YLABEL = 'Amplitude'

PLOT_SCALING = 1.5 #Scale y-axes to make plot look pretty
FIGURE_SIZE=(3,2)
PLOT_STYLE = 'seaborn'

plt.clf()


#********************************
#Define functions to plot here 
#Alternatively pass in csv file data
time = np.arange(START_TIME, STOP_TIME, TIME_STEP)
function_1 = np.cos(2*pi*time)
function_2 = np.sin(2*pi*time)

#***Main plot**************
fig = plt.figure(1,figsize=(FIGURE_SIZE))

#*****Subplot 1 ***********
ax1 = fig.add_subplot(121)  #Relative x-y position of subplot
ax1.plot(time, function_1)               
#Set length of axes 
ax1.set_xlim(START_TIME,STOP_TIME)
ax1.set_ylim(np.amin(function_1)*PLOT_SCALING, np.amax(function_1)*PLOT_SCALING)
#Add tiles and labels
ax1.set_title(AX1_TITLE)
ax1.set_xlabel(AX1_XLABEL)
ax1.set_ylabel(AX1_YLABEL)
ax1.grid(True) 
#**************************

#*******Subplot 2**********
ax2 = fig.add_subplot(122)
ax2.plot(time, function_2)
#Set length of axes
ax2.set_xlim(START_TIME,STOP_TIME)
ax2.set_ylim((np.amin(function_2)*PLOT_SCALING, np.amax(function_2)*PLOT_SCALING))
#Add titles & Labels
ax2.set_title(AX2_TITLE)
ax2.set_xlabel(AX2_XLABEL)
ax2.set_ylabel(AX2_YLABEL)
ax2.grid(True)
#************************

fig.tight_layout()
plt.style.use(PLOT_STYLE)
fig.suptitle(TITLE)
fig.set_size_inches(7,3)
fig.frameon = True
fig.subplots_adjust(left=0.1, right = 0.9, top=0.7, bottom = 0.15, 
                    hspace = 0.0, wspace =0.3 )

fig.show()