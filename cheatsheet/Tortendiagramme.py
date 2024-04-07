#Import libraries
import matplotlib.pyplot as plt

slices = [2,2,6,10,9]
sectors = ['Industrie', 'Lifestile', 'Consumer Goods', 'Commodities', 'Aerospace']
color = ['r','g','m','k','c']

plt.pie(slices, labels = sectors, colors = color )

plt.title('Business by Sector')

#Bring Graph to the fore front
plt.show()