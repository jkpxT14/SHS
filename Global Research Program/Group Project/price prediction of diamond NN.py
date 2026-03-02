import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

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
xTrain, xTest, yTrain, yTest=train_test_split(x, y, random_state=101) # test_size=0.3
# mean=xTrain.mean(axis=0)
# std=xTrain.std(axis=0)
# xTrain=(xTrain-mean)/std
# mean=xTest.mean(axis=0)
# std=xTest.std(axis=0)
# xTest=(xTest-mean)/std
scaler=MinMaxScaler()
xTrain=scaler.fit_transform(xTrain)
xTest=scaler.transform(xTest)
model=Sequential()
# model.add(Dense(64, activation='relu'))
# model.add(Dense(64, activation='relu'))
# model.add(Dense(1))
model.add(Dense(19, activation='relu'))
model.add(Dense(19, activation='relu'))
model.add(Dense(19, activation='relu'))
model.add(Dense(19, activation='relu'))
model.compile(optimizer='adam', loss='mse')
# history=model.fit(x=xTrain, y=yTrain.values, validation_data=(xTest, yTest.values), epochs=300)
history=model.fit(x=xTrain, y=yTrain.values, validation_data=(xTest, yTest.values), batch_size=128, epochs=400)
historyDataframe=pd.DataFrame(history.history)
print(historyDataframe)
plt.plot(range(1, 401), historyDataframe['val_loss'])
plt.show()