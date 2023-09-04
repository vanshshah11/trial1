import matplotlib.pyplot as plt
import numpy as np
 
 
# Creating datasets
np.random.seed(10)
data = np.random.normal(100, 20, 200)
 
fig = plt.figure(figsize =(10, 7))
 
# Creating plot
plt.boxplot(data)
 
# show plot
plt.show()
print("hello")