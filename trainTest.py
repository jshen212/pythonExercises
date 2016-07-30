import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# seeding the generator
np.random.seed(2)

# creating 2 normalized distributions
pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds

# scatter plotting the two sets of data
scatter(pageSpeeds, purchaseAmount)

# creating train sample
trainX = pageSpeeds[:80]
trainY = purchaseAmount[:80]


# creating test sample
testX = pageSpeeds[80:]
testY = purchaseAmount[80:]

# scatter plotting the training sets
scatter(trainX, trainY)
scatter(testX, testY)
x = np.array(trainX)
y = np.array(trainY)

# fitting the data to an 8th degree polynomial
p4 = np.poly1d(np.polyfit(x, y, 8))

# creating scatter plot with the polynomial visualization
xp = np.linspace(0, 7, 100)
axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0, 200])
plt.scatter(x, y)
plt.plot(xp, p4(xp), c='r')
plt.show()

# creating test samples
testx = np.array(testX)
testy = np.array(testY)

# scatter plotting the test samples with the polynomial visualization
axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0, 200])
plt.scatter(testx, testy)
plt.plot(xp, p4(xp), c='r')
plt.show()


# getting r2 value for test sample
r2 = r2_score(testy, p4(testx))

print r2

# getting r2 value for train sample
r2 = r2_score(np.array(trainY), p4(np.array(trainX)))

print r2
