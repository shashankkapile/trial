import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error,r2_score
import pandas as pd
import sklearn
from sklearn import tree
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt


data = pd.read_csv("buys.csv")
print(data.head())

encoder = preprocessing.LabelEncoder()
data = data.apply(encoder.fit_transform)
print(data.head())

train,test = train_test_split(data,test_size = 0.3,stratify = data['buys'])
train_X = train[train.columns[1:5]] 
train_Y = train['buys']
test_X = test[test.columns[1:5]]
test_Y = test['buys']


dt_x = list()
dt_y = list()

best_depth = 0
best_acc = 0

for i in range(2,11):
    dt = tree.DecisionTreeClassifier(max_depth=i, criterion='entropy')
    dt.fit(train_X, train_Y)
    predict = dt.predict(test_X)
    answer = sklearn.metrics.accuracy_score(test_Y, predict) * 100
    if answer > best_acc:
        best_acc = answer
        best_depth = i
    print('Accuracy of decision tree for max depth:', i, 'is:', answer, '%')
    dt_x.append(i)
    dt_y.append(answer)

plt.scatter(dt_x, dt_y)

plt.title('Decision tree variation of max depth vs accuracy')
plt.xlabel('Max depth of decision tree')
plt.ylabel('Accuracy of decision tree')
#plt.show()


print("Confusion Matrix :\n")
print(confusion_matrix(predict, test_Y, labels=[1, 0]))

dt = tree.DecisionTreeClassifier(max_depth=best_depth, criterion='entropy')
dt.fit(train_X, train_Y)

from sklearn import tree
import graphviz
dot_data = tree.export_graphviz(dt, out_file=None)

graph = graphviz.Source(dot_data)
graph.render("dt")



'''from sklearn import preprocessing

le = preprocessing.LabelEncoder()
# time 0 to 23 is 0 to 23
# sp high 0, max 1, median 2,
# jf green 1, yellow 3, red 2 , brown 0
# total_time moderate 1, high  0 , min 2
# yn yes 1, no 0

data.iloc[:,1]=le.fit_transform(data.iloc[:,1])
data.iloc[:,2]=le.fit_transform(data.iloc[:,2])
data.iloc[:,3]=le.fit_transform(data.iloc[:,3])
data.iloc[:,4]=le.fit_transform(data.iloc[:,4])

data
from sklearn.preprocessing import OneHotEncoder
enc = preprocessing.OneHotEncoder()

enc.fit(data.iloc[:,0:5])
onehotlabels = enc.transform(data.iloc[:,0:5]).toarray()
onehotlabels

# dataset=[pd.DataFrame(onehotlabels),data.iloc[:,5]]
dataset = pd.DataFrame(onehotlabels)
dataset['total_dist']=data.iloc[:,5] 
dataset['class']=data.iloc[:,6] 

display(dataset.iloc[:,0:37])
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import train_test_split

X = dataset.iloc[:,0:37].values
Y = dataset.iloc[:,37].values

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.2, random_state = 0)

classifier = DecisionTreeClassifier(random_state = 0)
classifier.fit(X_train,Y_train)

y_pred = classifier.predict(X_test)
'''