from pylab import *
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

scatter(pageSpeeds, purchaseAmount)

x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

# creates a polynomial regression with a 4th degree polynomial
p4 = np.poly1d(np.polyfit(x, y, 4))

# creates a line for data points between 0-7 seconds
xp = np.linspace(0, 7, 100)
plt.scatter(x, y)
plt.plot(xp, p4(xp), c='r')
plt.show()


r2 = r2_score(y, p4(x))

print r2
