import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# creates an incomes variable with a random normal distribution centered around 27000, std of 15000, and 10000 values
incomes = np.random.normal(27000, 15000, 10000)

# calculates the mean of the incomes
np.mean(incomes)

# creates a histogram based on incomes with 50 values to a bucket
plt.hist(incomes, 50)
plt.show()

# calculates the median of the incomes
np.median(incomes)

# appends 20000 to the incomes values
incomes = np.append(incomes, [20000])

# calculates the new median and mean of the incomes
np.median(incomes)
np.mean(incomes)

# creates a random set of 500 values between 18 and 90
ages = np.random.randint(18, high=90, size=500)
print ages

# calculates the mode of the ages
stats.mode(ages)
