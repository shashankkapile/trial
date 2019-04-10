import numpy as np
import pandas as pd 

from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
buy = pd.read_csv('buys.csv')

buy['age'],_=pd.factorize(buy['age'])
buy['income '],_=pd.factorize(buy['income '])
buy['gender'],_=pd.factorize(buy['gender'])
buy['marital_status'],_=pd.factorize(buy['marital_status'])
buy['buys'],_=pd.factorize(buy['buys'])

X = buy.values[:, 0:4] 
Y = buy.values[:, 4] 
labels=['age','income','gender','marital_status']
print(X)
from sklearn import tree
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf=clf.fit(X,Y)


from graphviz import pydotplus as pdd
from IPython.display import Image
dot_data = tree.export_graphviz(clf, out_file=None, 
                                feature_names=labels,class_names=['no', 'yes'], filled = True)

graph = pdd.graph_from_dot_data(dot_data)  

Image(graph.create_png())
graph.write_png("dtree.png")