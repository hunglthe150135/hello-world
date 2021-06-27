print("Hello World")

import matplotlib.pyplot as plt
probability = [0.25127, 0.17005, 0.14721, 0.23465, 0.19682]
point = ['0-2', '2.2-4', '4.2-6', '6.2-8', '8.2-10'] #sample names
plt.bar(point, probability)
plt.xticks(point)
plt.yticks(probability) 
plt.xlabel('Point')
plt.ylabel('Probability')
plt.show()