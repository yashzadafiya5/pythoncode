# 26. Box Plot using Python 
# Import libraries
import matplotlib.pyplot as plt
import numpy as np
 
 
# Creating dataset
np.random.seed(10)
data = np.random.normal(20, 5, 20)
 
fig = plt.figure(figsize =(2, 2))
 
# Creating plot
plt.boxplot(data)
 
# show plot
plt.show()