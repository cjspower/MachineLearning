import numpy as np
def readData(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split(' ')
        curLine = map(float, curLine)
        dataMat.append(curLine)
    return np.array(dataMat)

def dist(A, B):
    "compute the eclud distance of two data points"
    return np.sqrt(sum(np.power(A-B,2)))
    
def randomStart(dataSet, k):
    "create k random cluster center"
    n = np.shape(dataSet)[1]
    centroids = np.zeros((k,n))
    print centroids
    for i in xrange(n):
        minI = min(dataSet[:,i])
        rangeI = float(max(dataSet[:,i])-minI)
        centroids[:,i] = (minI + rangeI*np.random.rand(k,1))[:,0]
    return centroids
    
def kmeansCluster(dataSet, k, distMeas = dist, createCent = randomStart):
    "kmeans algorithm"
    dataLen = np.shape(dataSet[0])
    clusterAssment = np.zeros((dataLen,2))
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in xrange(dataLen):
            minDist = inf
            minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j],dataSet[i])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i][0] != minIndex:
                clusterChanged = True
            clusterAssment[i] = np.array([minIndex, minDist**2])
        print centroids
        for cent in xrange(k):
                    

    
    
a = 1.1
b = 2
print np.array([a,b])
    