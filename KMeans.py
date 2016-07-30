from numpy import random, array
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from numpy import random, float

def createClusteredData(N, k):
#createss consistent random seed to start with
    random.seed(10)
    #creates a set number of points, per cluster
    pointsPerCluster = float(N)/k
    X = [];

    for i in range (k):
        # creates a random income centroid
        incomeCentroid = random.uniform(20000.0, 200000.0)
        # creates a random age centroid
        ageCentroid = random.uniform(20.0, 70.0)
        for j in range(int(pointsPerCluster)):
            # adds a normalized income centroid with std of 10000 and age centroid with std of 2 to the X array
            X.append([random.normal(incomeCentroid, 10000.0), random.normal(ageCentroid, 2.0)])
    X = np.array(X)
    return X

# creates 100 random people in 5 clusters
data = createClusteredData(100, 5)
# creates a k-means model with 5 clusters
model = KMeans(n_clusters=5)

# creates a model that fits the data to a normalized scale
model = model.fit(scale(data))

# prints out the k-means categorization labels
print model.labels_

# visualizes the data points and clusters
plt.figure(figsize=(8, 6))
plt.scatter(data[:,0], data[:,1], c=model.labels_.astype(float))
plt.show()
