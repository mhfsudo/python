import matplotlib.pyplot as plt

#Data
population_ages = [22,55,71,13,13,56,7,71,67,33,32,21,22,53,33,11,13,56,23,71]

#bins to cout for age groups
bins = [0,10,20,30,40,50,60,70,80]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

#Description
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Age distribution in population')

#bring Graph to the fore front
plt.show()