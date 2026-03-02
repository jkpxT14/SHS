import matplotlib.pyplot as plt
import csv

# def avg(x) :
#     return sum(x)/len(x)

data=csv.reader(open('C:/Users/jkpxtwin/Desktop/SchoolPy/2022dataset/seoulrain.csv', 'r', encoding='UTF-8'))
next(data)
data=list(data)
# rain=[]
# result=[]
# for i in range(26) :
#     rain.append([])
# for row in data :
#     if row[1]=='기상청' and int(row[2][5:7])==8 :
#         rain[int(row[2][:4])-1997].append(float(row[3]))
# for i in range(26) :
#     result.append(avg(rain[i]))
# plt.figure(dpi=100)
# plt.style.use('ggplot')
# plt.title('A')
# plt.bar(range(1997, 2023), result)
# plt.xticks(range(1997, 2023), range(1997, 2023), rotation=75)
# plt.show()
rain=[]
rain0=[]
for row in data :
    if row[1]=='서초' :
        rain.append(float(row[3]))
        if(float(row[3])>0) :
            rain0.append(float(row[3]))
plt.pie([len(rain)-len(rain0), len(rain0)], autopct='%.2f%%', labels=['RainNo', 'rainYes'])
plt.legend()
plt.show()