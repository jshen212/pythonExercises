import numpy as np
import matplotlib.pyplot as plt

# creates a set of 10000 random incomes around 100 with std of 20
incomes = np.random.normal(100, 20, 10000)

# creates histogram of the incomes with 50 buckets
plt.hist(incomes, 50)
plt.show()

# calculates the standard deviation
incomes.std()

# calculates the variance
incomes.var()


incomes = np.random.normal(100, 10, 1000)

plt.hist(incomes, 50)
plt.show()

incomes.std()
incomes.var()
