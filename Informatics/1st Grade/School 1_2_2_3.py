import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('C:/Users/jkpxtwin/Desktop/SchoolPy/2022dataset/신검데이터m.csv')
# print(df)
x=df['신장 센티미터']
y=df['몸무게 킬로그램']
# plt.scatter(x, y)
# plt.hist(x, bins=200)
# plt.hist(y, bins=200)
# plt.boxplot(x)
# plt.show()
# plt.boxplot(y)
# plt.show()
# print(df[df['몸무게 킬로그램']<10])
idx=df[df['몸무게 킬로그램']==0].index
df=df.drop(idx)
# print(df[df['몸무게 킬로그램']<10])
x=df['신장 센티미터'].values.reshape(-1, 1)
y=df['몸무게 킬로그램'].values
plt.scatter(x, y)
plt.show()