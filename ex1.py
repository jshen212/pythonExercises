import numpy as np
import matplotlib.pyplot as plt

#creates a normal distribution of values centered around 100, std of 20, and 10000 values
incomes = np.random.normal(100, 20, 10000)

#finds the mean and median of the incomes data set
print np.mean(incomes)
print np.median(incomes)

#creates a histogram with 50 values to a bucket
plt.hist(incomes, 50)
plt.show()
