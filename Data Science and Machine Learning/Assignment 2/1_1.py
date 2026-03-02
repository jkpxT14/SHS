# Seoul High School Jungwoo K.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x=np.array([[74], [81], [94], [68], [64], [70], [83], [94], [71], [74]])
y=np.array([71, 78, 90, 68, 66, 72, 89, 92, 78, 80])
# y=np.array([[71], [78], [90], [68], [66], [72], [89], [92], [78], [80]])
# plt.scatter(x, y, color='blue')
# plt.xlabel("A")
# plt.ylabel("B")
# plt.show()
print(np.corrcoef(x.reshape(len(y)), y))
linReg=LinearRegression(fit_intercept=True)
model=linReg.fit(x, y)
w=model.coef_
b=model.intercept_
print(w, b)
plt.plot(x, y, 'bo', label="Real")
plt.plot(x, np.array(w*x+b), 'r', label="Pred")
plt.xlabel("A")
plt.ylabel("B")
plt.legend()
plt.show()
xNew=np.array([[80], [90]])
yNew=model.predict(xNew)
print(yNew)