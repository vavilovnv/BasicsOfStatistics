# https://stepik.org/lesson/8090/step/2?unit=1369
# Интерпретация результатов регрессионного анализа с несколькими независимыми переменными и визуализацией
# плоскости модели

from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import pandas as pd, numpy as np


def f(x, y):
    return lm.params.Intercept + lm.params.hs_grad * x + lm.params.metro_res * y


data = pd.read_csv('http://d396qusza40orc.cloudfront.net/statistics/lec_resources/states.csv')

# инициализируем параметры модели
X = data[['white', 'hs_grad']]
y = data['poverty']
reg = LinearRegression().fit(X, y)
lm = smf.ols(formula='poverty ~ metro_res + hs_grad', data=data).fit()

# зададим масштаб и подписи осей графика
fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection='3d')
ax.set_xlabel('Higher education(%)')
ax.set_ylabel('White(%)')
ax.set_zlabel('Poverty(%)')

# выведем плоскость для нашей модели
d1, d2 = list(), list()
for x in np.linspace(min(data.white), max(data.white), 100):
    for y in np.linspace(min(data.hs_grad), max(data.hs_grad), 100):
        d1.append(x)
        d2.append(y)
d1, d2 = np.array(d1).reshape(-1, 1), np.array(d2).reshape(-1, 1)
p = reg.predict(np.concatenate([d1, d2], axis=1))
ax.plot_trisurf(d2.ravel(), d1.ravel(), p.ravel(), alpha=0.2)

# выведем точки над плоскостью нашей модели
data_above_serf = data[data.poverty >= f(data.hs_grad, data.metro_res)]
ax.scatter(data_above_serf.hs_grad, data_above_serf.metro_res, data_above_serf.poverty, c='g', marker='o')

# выведем точки под плоскостью нашей модели
data_below_serf = data[data.poverty < f(data.hs_grad, data.metro_res)]
ax.scatter(data_below_serf.hs_grad, data_below_serf.metro_res, data_below_serf.poverty, c='r', marker='o')

plt.show()
