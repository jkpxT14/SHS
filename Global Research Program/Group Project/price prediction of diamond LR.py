import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df=pd.read_csv('C:/Users/jkpxtwin/Desktop/23GRP/GroupProject/diamonds.csv')
df=df.drop('Unnamed: 0', axis=1)
x=df.drop('price', axis=1)
cutDict={'Ideal': 5.0, 'Premium': 4.0, 'Very Good': 3.0, 'Good': 2.0, 'Fair': 1.0}
colorDict={'D': 7.0, 'E': 6.0, 'F': 5.0, 'G': 4.0, 'H': 3.0, 'I': 2.0, 'J': 1.0}
clarityDict={'IF': 8.0, 'VVS1': 7.0, 'VVS2': 6.0, 'VS1': 5.0, 'VS2': 4.0, 'SI1': 3.0, 'SI2': 2.0, 'I1': 1.0}
x=x.replace({'cut': cutDict})
x=x.replace({'color': colorDict})
x=x.replace({'clarity': clarityDict})
y=df['price']
xTrain, xTest, yTrain, yTest=train_test_split(x, y) # test_size=0.3
model=LinearRegression()
model.fit(xTrain, yTrain)
yPredict=model.predict(xTest)
plt.scatter(yTest, yPredict, alpha=0.4)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Multiple Linear Regression')
plt.show()
print(model.score(xTrain, yTrain))