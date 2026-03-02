import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df1=pd.read_csv('https://raw.githubusercontent.com/greatsong/2022dataset/main/mosq.csv')
df2=pd.read_csv('https://raw.githubusercontent.com/greatsong/2022dataset/main/ta.csv')
# print(df1)
# print(df2)
df3=pd.merge(df1, df2, on='날짜')
# print(df3)
df4=df3.drop(['지점'], axis=1)
# print(df4)
# print(df4.describe())
df=df4.dropna()
# print(df.describe())
# print(df.corr())
df['date']=pd.to_datetime(df['날짜'])
# df['dayofyear']=df.date.dt.dayofyear # df.date
df['dayofyear']=df['date'].dt.dayofyear # df['date']
# print(df[df['모기지수(주거지)']==15])
df=df[df['date']>='2020-05-01']
df=df[df['모기지수(주거지)']!=15]
# print(df)
# print(df.date)
# print(df.corr())
model=LinearRegression().fit(df['최저기온(℃)'].values.reshape(-1, 1), df['모기지수(주거지)'].values.reshape(-1, 1))
x=df['최저기온(℃)']
y=df['모기지수(주거지)']
# plt.scatter(x, y)
# plt.show()
# plt.plot(x, x*model.coef_[0]+model.intercept_, color='r')
# plt.show()
temp=float(input('오늘의 최저 기온을 입력해주세요 : '))
pred=temp*model.coef_[0]+model.intercept_
# print(type(pred[0]))
print(f'주거지 예상 모기지수는 {pred[0]:.2f}입니다.')