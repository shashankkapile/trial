import matplotlib.pyplot as plt
import csv

def loadDS(filename, X=[], Y=[]):
    with open(filename, 'r') as csvf:
        lines = csv.reader(csvf)
        dataset = list(lines)
        L = len(dataset)
        for x in range(1, L):
            X.append(float(dataset[x][0]))
            Y.append(float(dataset[x][1]))


def kmean(X=[], Y=[], m1=[], m2=[], C1={}, C2={}):

    while True :
        C1['x'].clear()
        C1['y'].clear()
        C2['x'].clear()
        C2['y'].clear()
        for i in range(len(X)):
            if abs((pow(m1[0]-X[i], 2)+pow(m1[1]-Y[i], 2)) < (pow(m2[0]-X[i], 2)+pow(m2[1]-Y[i], 2))):
                C1['x'].append(X[i])
                C1['y'].append(Y[i])
            else:
                C2['x'].append(X[i])
                C2['y'].append(Y[i])
        temp1 = m1.copy()
        temp2 = m2.copy()
        l1 = len(C1['x'])
        l2 = len(C2['x'])
        if l1 != 0:
            m1[0] = round((sum(C1['x'])/l1), 2)
            m1[1] = round((sum(C1['y'])/l1), 2)
        if l2 != 0:
            m2[0] = round((sum(C2['x'])/l2), 2)
            m2[1] = round((sum(C2['y'])/l2), 2)
        if temp1[0] == m1[0] and temp1[1] == m1[1] and temp2[0] == m2[0] and temp2[1] == m2[1]:
            break




def main():

    X = []   # X cordinate
    Y = []   # Y cordinate
    m1 = []  # center of cluster C1
    m2 = []  # center of cluster C2
    C1 = {'x': [], 'y': []}  # cluster 1
    C2 = {'x': [], 'y': []}  # cluster 2

    loadDS('kmean.csv', X, Y)
    #print(X)
    plt.figure(1)
    plt.axis('equal')
    plt.scatter(X, Y, color='green')

    m1.append(X[0])   # point P1
    m1.append(Y[0])
    m2.append(X[7])   # point P8
    m2.append(Y[7])

    kmean(X, Y, m1, m2, C1, C2)
    plt.figure(2)
    plt.scatter(C1['x'], C1['y'], color='red')
    plt.scatter(C2['x'], C2['y'], color='blue')
    plt.plot(m1[0], m1[1], 's')
    plt.plot(m2[0], m2[1], 's')
    for x, y in zip(C1['x'], C1['y']):
        plt.plot([m1[0], x], [m1[1], y])
    for x, y in zip(C2['x'], C2['y']):
        plt.plot([m2[0], x], [m2[1], y])
    plt.axis('equal')
    plt.show()


main()