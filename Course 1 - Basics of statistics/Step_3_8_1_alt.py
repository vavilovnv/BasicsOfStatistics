# https://stepik.org/lesson/8090/step/2?unit=1369
# Интерпретация результатов регрессионного анализа с несколькими независимыми переменными и визуализацией
# плоскости модели

from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('http://d396qusza40orc.cloudfront.net/statistics/lec_resources/states.csv')

X = data[['white', 'hs_grad']]
y = data['poverty']

reg = LinearRegression().fit(X, y)

d1, d2 = list(), list()
for x in np.linspace(min(data['white']), max(data['white']), 100):
    for y in np.linspace(min(data['hs_grad']), max(data['hs_grad']), 100):
        d1.append(x)
        d2.append(y)
d1 = np.array(d1).reshape(-1, 1)
d2 = np.array(d2).reshape(-1, 1)
p = reg.predict(np.concatenate([d1, d2], axis=1))

fig = plt.figure(figsize=(8, 8))

ax = plt.axes(projection='3d')
ax.scatter(data['hs_grad'], data['white'], data['poverty'], s=50)
ax.plot_trisurf(d2.ravel(), d1.ravel(), p.ravel(), alpha=0.2)
ax.set_xlabel('Higher education(%)')
ax.set_ylabel('White(%)')
ax.set_zlabel('Poverty(%)')
ax.elev = 10
ax.azim = -60

plt.show()
