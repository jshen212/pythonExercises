import numpy as np
import matplotlib.pyplot as plt

# creates a random set of 10000 values centered around 0 with a std of 0.5
vals = np.random.normal(0, 0.5, 10000)

# creates a histogram of the vals with 50 vals to a bucket
plt.hist(vals, 50)
plt.show()

# calculates the 50th percentile value
np.percentile(vals, 50)

# calculates the 90th percentile value
np.percentile(vals, 90)

# calculates the 20th percentile value
np.percentile(vals, 20)

# creates a new set of vals around 0 with a std of 0.5
vals = np.random.normal(0, 0.5, 10000)
plt.hist(vals, 50)
plt.show()

# calculates the 92nd percentile value
np.percentile(vals, 92)

# calculates the 25th percentile value
np.percentile(vals, 25)
