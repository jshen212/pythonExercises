import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import expon
from scipy.stats import binom
from scipy.stats import poisson

# creates a uniform set of 100000 values from -10 to 10
values = np.random.uniform(-10, 10, 100000)
plt.hist(values, 50)
plt.show()

# creates a range from -3 to 3 in increments of 0.001
x = np.arange(-3, 3, 0.001)

# plots a graph of the probability density function
plt.plot(x, norm.pdf(x))

mu = 5
sigma = 2
values = np.random.normal(mu, sigma, 10000)
plt.hist(values, 50)
plt.show()

# creates exponential probability density function
x= np.arange(0, 10, 0.001)
plt.plot(x, expon.pdf(x))

# creates binomial probability mass function
n, p = 10, 0.5
x= np.arange(0, 10, 0.001)
plt.plot(x, binom.pmf(x, n, p))

# creates poisson probability mass function
# gets the odds of 500 NOT happening
mu = 500
x = np.arange(400, 600, 0.5)
plt.plot(x, poisson.pmf(x, mu))
