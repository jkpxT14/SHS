# Seoul High School Jungwoo K.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x=[[68, 74, 69],
[83, 81, 76],
[100, 94, 84],
[71, 68, 67],
[63, 64, 66],
[70, 70, 70],
[77, 83, 90],
[86, 94, 90],
[76, 71, 77],
[64, 74, 84]]
y=np.array([71, 78, 90, 68, 66, 72, 89, 92, 78, 80])
linReg=LinearRegression(fit_intercept=True)
model=linReg.fit(x, y)
w=model.coef_
b=model.intercept_
print(w, b, model.score(x, y))
xNew=np.array([[80, 80, 80], [90, 80, 70], [70, 80, 90]])
yNew=model.predict(xNew)
print(yNew)