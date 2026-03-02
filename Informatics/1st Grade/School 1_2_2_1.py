import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

df=pd.read_csv('https://raw.githubusercontent.com/greatsong/2022dataset/main/seoultemp(year%2C2021).csv')
# print(df)
# df.info()
df=df.fillna(method='bfill')
# df.info()
year=df['년']
temp=df['평균기온(℃)']
# plt.plot(year, temp)
# plt.scatter(year, temp)
# plt.show()
year=np.reshape(year.values, (-1, 1))
temp=np.reshape(temp.values, (-1, 1))
# print(year)
# print(temp)
model0=LinearRegression().fit(year, temp)
# print(model0.coef_, model0.intercept_)
# y_pred=int(input('예측하고 싶은 연도를 입력해주세요 : '))
# pred=model0.coef_*y_pred+model0.intercept_
# print(pred)
# print(f'서울의 {y_pred}년도 예상 평균 기온 : {pred[0][0]:.2f}도') # pred
# print(year[-50])
# plt.scatter(year[:-50], temp[:-50], marker='^', color='b')
# plt.scatter(year[-50:], temp[-50:], marker='o', color='r')
# plt.show()
plt.figure(dpi=100)
model1=LinearRegression().fit(year, temp)
model2=LinearRegression().fit(year[:-50], temp[:-50])
model3=LinearRegression().fit(year[-50:], temp[-50:])
x1=np.arange(1907, 2051).reshape(-1, 1)
x2=np.arange(1907, 1972).reshape(-1, 1)
x3=np.arange(1972, 2051).reshape(-1, 1)
y1=model1.predict(x1)
y2=model2.predict(x2)
y3=model3.predict(x3)
plt.scatter(year[:-50], temp[:-50], marker='^', color='b')
plt.scatter(year[-50:], temp[-50:], marker='o', color='r')
plt.plot(x1, y1, 'g', label='1907~2050')
plt.plot(x2, y2, 'b:', label='1907~1971')
plt.plot(x3, y3, 'r--', label='1972~2050')
plt.legend()
# print(type(model1))
print(y1[143][0], type(y1[143][0]))
plt.show()