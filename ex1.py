import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#creates a normal distribution of values centered around 100, std of 20, and 10000 values
incomes = np.random.normal(100, 20, 10000)

#finds the mean and median of the incomes data set
print np.mean(incomes)
print np.median(incomes)

#creates a histogram with 50 values to a bucket
plt.hist(incomes, 50)
plt.show()

#reassigns incomes variable to a new normal distribution
incomes = np.random.normal(100, 2000, 10000)

#adds an outlier to the incomes values
incomes = np.append(incomes, [1000000000])

#calculates the new mean of the incomes
np.mean(incomes)

#calculates the new mode of the incomes
stat.mode(incomes)

#reassigns the incomes variable to a new normal distribution
incomes = np.random.normal(1000, 200, 10000)

#calculates the new mode of the incomes
stats.mode(incomes)

#creates an ages varaible with a random data set between 20 to 100 with 2000 values
ages = np.random.randint(20, high=100, size=2000)

#calculates the new mode of the ages
stats.mode(ages)
