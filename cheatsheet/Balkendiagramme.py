#Import libraries
import matplotlib.pyplot as plt
import numpy as np

x = [2,4,6,8,10]
y = [5,7,4,6,2]
x2 = [1,3,5,7,9]
y2 = [4,6,2,5,7]

plt.bar(x, y, label='Balken 1')
plt.bar(x2, y2, label='Balken 2',color="r")

plt.ylabel('Count')
plt.title('Statistic')
plt.legend()

#Adjust hight of the Diagramm just for the legend
plt.yticks( np.arange(11) )
#Adjust x-ticks
plt.xticks( np.arange(11) )

#bring Graph to the fore front
plt.show()