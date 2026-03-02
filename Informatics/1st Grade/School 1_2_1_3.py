import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('C:/Users/jkpxtwin/Desktop/SchoolPy/2022dataset/seoulrain.csv', index_col='일시')
df2=df[df['지점명']=='서초']
df3=df2[(df2.index>='2022-08-01') & (df2.index<='2022-08-11')]
df3['일강수량(mm)'].plot.bar()
plt.show()