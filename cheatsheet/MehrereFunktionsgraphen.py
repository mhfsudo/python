#Import libraries
import numpy as np
import matplotlib.pyplot as plt

#Define x-Axis. numpy.linspace(start, stop, number of samples)
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)

#Define Graphs
y1 = np.sin(3* x +1)
y2 = (2*x**5 + 4.8*x**3 + 1.2*x**2 + x + 1)*np.exp(-x**2)

#assign plot
ax = plt.gca()

#Adjust axes
# Make upper and right axis invisible
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
#move lower axis to y=0 :
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
#move left axis to y=0 x == 0:
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.plot(x, y1)
plt.plot(x, y2)

#Bring Graph to the fore front
plt.show()