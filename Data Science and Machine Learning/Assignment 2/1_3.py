# Seoul High School Jungwoo K.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

x=np.array([[74], [81], [94], [68], [64], [70], [83], [94], [71], [74]])
y=np.array([1, 1, 1, 0, 0, 0, 1, 1, 0, 1])

logReg=LogisticRegression(solver='lbfgs')
model=logReg.fit(x, y)
w=model.coef_
b=model.intercept_
print(w, b)

def H(x):
    return 1/(1+np.exp(-(w*x+b)))

yPred=np.where(H(x)>=0.5, 1, 0)

xIn=np.arange(x.min(), x.max(), 0.5)
Hx=H(xIn).reshape(-1, 1)
plt.plot(x, y, 'bo', label="Train")
plt.plot(xIn, Hx, 'g', label="H")
plt.plot(x, yPred, 'rx', label="P")
plt.xlabel("A")
plt.ylabel("B")
plt.legend(loc='right')
plt.show()

xNew=np.array([[72], [73]])
yNew=model.predict(xNew)
# yNew=np.where(H(xNew)>=0.5, 1, 0)
print(yNew)