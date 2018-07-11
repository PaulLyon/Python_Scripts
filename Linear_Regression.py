# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 10:14:41 2018

@author: Paul Lyon

Linear Regression Exercise

Imports a csv file and performs linear regression (in the form Y=mX+c)
 & displays equation on the chart in a sensible place next to the data.

"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

PATH =""                     # Directory PATH to csv file location if needed
COLUMN_X = 0                 # x axis data in csv file
COLUMN_Y = 1                 # y axis data in csv file
NO_OF_POINTS = 1000          # No. of points to calculate regression fit

LINE_FIT_SCALE_FACTOR = 1.1  # Extends range of chart so it looks nice
TEXT_ORIGIN_SCALING = 0.25   # Offsets text on chart from line
PLOT_SCALING = 1.5           # Scale y-axes to make plot look pretty
FIGURE_SIZE=(7,3)          
PLOT_STYLE = 'seaborn'       # Console: print(plt.style.available) 
SIG_FIG_3 = '.3g'            # N=3 No. of significant figures displayed

TITLE = 'Random Data'
XLABEL = 'Independent Variable'
YLABEL = 'Dependent Variable'

#regression_data.csv is a csv file with numeric data in COLUMN_0 & COLUMN_1
csv_file = PATH + 'regression_data.csv'
#****************************

#*** x-y scatter plot of csv_file data****
csv_data = np.genfromtxt(csv_file, delimiter=",")

x_data=csv_data[:,COLUMN_X].reshape(-1,1)
y_data=csv_data[:,COLUMN_Y].reshape(-1,1)
#*****************************

#***Calc line fit & plot onto chart***
regression_model = LinearRegression(fit_intercept=True)
regression_model.fit(x_data, y_data)

x_fit = np.linspace(0, max(x_data)*LINE_FIT_SCALE_FACTOR, NO_OF_POINTS)
y_fit = regression_model.predict(x_fit[:, np.newaxis])
#******************************

#***Calculate Y=mX+c coeff and intercept****
m = regression_model.coef_[0,0]
c = regression_model.intercept_[0]
#******************************

#***Calculates sensible origin for displaying equation on chart
#   so it doesnt sit over the data
x_txt_origin = np.median(x_data) + (TEXT_ORIGIN_SCALING*(max(x_data)-min(x_data)))
y_txt_origin = np.median(y_data)
#************************************************************

plt.figure(figsize=FIGURE_SIZE)

plt.scatter(x_data, y_data)

plt.plot(x_fit, y_fit)

plt.tight_layout()
plt.style.use(PLOT_STYLE)
plt.suptitle(TITLE)
plt.xlabel(XLABEL)
plt.ylabel(YLABEL)
plt.frameon = True
plt.subplots_adjust(left=0.1, right = 0.9, top=0.9, bottom = 0.15, 
                    hspace = 0.0, wspace =0.3 )

# Chooses between 'Y= mX + c' and 'Y= mX - c' and displays equation on chart
if c>0: #Y=mX + c
    equation='y = '+str(format(m,SIG_FIG_3))+'x + '+str(format(c,SIG_FIG_3))
    plt.text(x_txt_origin, y_txt_origin, equation)

else: #Y=mX - c
    equation='y = '+str(format(m,SIG_FIG_3))+'x '+str(format(c,SIG_FIG_3))
    plt.text(x_txt_origin, y_txt_origin, equation)
#*******************************

plt.show()