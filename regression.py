import matplotlib.pyplot as plt
import pandas as pd

# Read Dataset
dataset=pd.read_csv("ass1data.csv")
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,1].values

# Import the Linear Regression and Create object of it
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X,Y)
Accuracy=regressor.score(X,Y)*100
print("Accuracy :")
print(Accuracy)

# Predict the value using Regressor Object
y_pred=regressor.predict([[10]])
print(y_pred)

# Take user input
hours=int(input('Enter the no of hours'))

#calculate the value of y
eq=regressor.coef_*hours+regressor.intercept_
y='%f*%f+%f' %(regressor.coef_,hours,regressor.intercept_)
print("y :")
print(y)

print("Risk Score : ", eq[0])
plt.plot(X,Y,'o')
plt.plot(X,regressor.predict(X));
plt.show()

