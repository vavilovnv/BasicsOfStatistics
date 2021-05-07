# https://stepik.org/lesson/8089/step/3?unit=1368
# Интерпретация результатов регрессионного анализа зависимости уровня бедности от уровня образования

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


data = pd.read_csv('http://d396qusza40orc.cloudfront.net/statistics/lec_resources/states.csv')
poverty_grad = data[['hs_grad', 'poverty']].describe()
print(poverty_grad.describe())

a = data['poverty'].to_numpy().reshape(-1, 1)
b = data['hs_grad'].to_numpy().reshape(-1, 1)

LR = LinearRegression()
model = LR.fit(b, a)
print('Модель зависимости бедности от уровня образования', f'y = {model.intercept_}{model.coef_}x')
y = [model.intercept_ + model.coef_[0]*i for i in b]

plt.scatter(b, a)
plt.plot(b, y)
plt.title('Корреляция', fontsize=14)
plt.xlabel("Уровень образования %")
plt.ylabel("Уровень бедности %")
plt.show()
