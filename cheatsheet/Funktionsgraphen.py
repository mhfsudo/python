#Import libraries
import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5],[2,2,6,10,9])

plt.xlabel('Time [s]')
plt.ylabel('Speed [m/s]')
#add '\n' for new line to create a simple subtitle
plt.title('Speed Boster\nDevelopment Project')

#Bring Graph to the fore front
plt.show()