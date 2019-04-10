import math
import operator
import csv

def loadDS(filename, split, trainSet=[], testSet=[]):
    with open(filename, 'r') as csvFile:
        lines = csv.reader(csvFile)
        dataset = list(lines)
        L=len(dataset);
        for x in range(1, L):
            if x <= split:
                trainSet.append(dataset[x])
            else:
                testSet.append(dataset[x])


def ecldDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((float(instance1[x])-float(instance2[x])), 2)
    return math.sqrt(distance)

def getNeighbour(trainSet, testSet, k, type):
    distances = []
    for x in range(len(trainSet)):
        dist = ecldDistance(testSet[0], trainSet[x], length=2)
        distances.append((trainSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbours = []
    for x in range(k):
        if type == 's':
            neighbours.append(distances[x][0])
        else:
            neighbours.append((distances[x][0], (1/distances[x][1])))
    return neighbours

def getResponse(neighbours, type):
    votes = {}
    for x in range(len(neighbours)):
        if type == 's':
            response = neighbours[x][-1]
            if response in votes:
                votes[response] += 1
            else:
                votes[response] = 1
        if type == 'w':
            response = neighbours[x][0][-1]
            if response in votes:
                votes[response] += neighbours[x][1]
            else:
                votes[response] = neighbours[x][1]
    sortVote = sorted(votes.items(), key=operator.itemgetter(1), reverse=True)
    print(sortVote)
    return sortVote[0][0]




def main():
    trainSet = []
    testSet = []
    split = 6
    loadDS('knn.csv', split, trainSet, testSet)
    print('Training Set : ')
    print(trainSet)
    print('Testing Set : ')
    print(testSet)
    print('Distance : ')
    print(ecldDistance(testSet[0], trainSet[5], length=2))

    print('Neighbours : ')
    N = getNeighbour(trainSet, testSet, k=3, type='s')
    print(N)
    print('Simple voting and Class of (6,6) : ')
    print(getResponse(N, type='s'))

    print('Neighbours with weight : ')
    N = getNeighbour(trainSet, testSet, k=3, type='w')
    print(N)
    print('Weighted voting and Class of (6,6) : ')
    print(getResponse(N, type='w'))

main()




