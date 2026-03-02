# Importing libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Reading CSV and converting object data to integers + setting x and y variables
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
# Training the model
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
# A function to ask the user for input and return a data point
def get_data_point():
    carat = float(input("Enter carat: "))
    cut = input("Enter cut: ")
    color = input("Enter color: ")
    clarity = input("Enter clarity: ")
    depth = float(input("Enter depth: "))
    table = float(input("Enter table: "))
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    z = float(input("Enter z: "))
    return [carat, cut, color, clarity, depth, table, x, y, z]

# Asking the user for input and create a data point
data_point = get_data_point()

# Converting the data point to the same format as the training data
cutDict={'Ideal': 5, 'Premium': 4, 'Very Good': 3, 'Good': 2, 'Fair': 1}
colorDict={'D': 7, 'E': 6, 'F': 5, 'G': 4, 'H': 3, 'I': 2, 'J': 1}
clarityDict={'IF': 8, 'VVS1': 7, 'VVS2': 6, 'VS1': 5, 'VS2': 4, 'SI1': 3, 'SI2': 2, 'I1': 1}
try:
    data_point[1] = cutDict[data_point[1]]
except KeyError:
    print("Invalid cut")
try:
    data_point[2] = colorDict[data_point[2]]
except KeyError:
    print("Invalid color")
try:
    data_point[3] = clarityDict[data_point[3]]
except KeyError:
    print("Invalid clarity")

# Predicting the price
price = model.predict([data_point])
print(f"Predicted price: {price[0]:.2f}")