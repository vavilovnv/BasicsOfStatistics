# https://stepik.org/lesson/8089/step/5?unit=1368
# Интерпретация результатов регрессионного анализа зависимости уровня бедности от уровня образования

import pandas as pd, numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

data = pd.read_csv('http://d396qusza40orc.cloudfront.net/statistics/lec_resources/states.csv')

# расчет ковариационной матрицы двух векторов, на выходе ковариация и дисперсии каждого из массивов,
X = data['hs_grad']
Y = data['poverty']
ssxm, ssxym, ssyxm, ssym = np.cov(X, Y).flat

# расчет корреляции по формуле из урока 3_1 третье видео: r = cov/stdx*stdy,
# т.к. в ковариационной матрице у нас дисперсии, то в знаменателе нужно взять квадратный корень
if ssxm == 0 or ssym == 0:
    r = 0
else:
    r = ssxym / (ssxm * ssym) ** 0.5

# расчет slope и intercept из урока 3_3 второе видео: slope = (stdy/stdx) * r
slope = r * (ssym / ssxm) ** 0.5
intercept = np.mean(Y) - slope * np.mean(X)

df = len(X) - 2
# расчет t - значения, вероятности p и стандартной ошибки для X параметра взято отсюда:
# https://github.com/scipy/scipy/blob/v1.4.1/scipy/stats/_stats_mstats_common.py#L15-L144
tx = r * np.sqrt(df / ((1.0 - r) * (1.0 + r)))
sterrestx = np.sqrt((1 - r ** 2) * ssym / ssxm / df)
px = 2 * stats.t.sf(np.abs(tx), df)

# Вычислим сумму квадратов по параметру X
s = [i ** 2 for i in X]
sterresty = (sterrestx ** 2 / 51 * sum(s)) ** 0.5

# расчет t - значения, вероятности p и стандартной ошибки для Y параметра взято отсюда:
# https://en.wikipedia.org/wiki/Simple_linear_regression
ty = intercept / sterresty
py = 2 * stats.t.sf(np.abs(ty), df)

# рассчет F-статистики взято отсюда:
# https://www.chem-astu.ru/science/reference/fischer.html
F = r ** 2 / (1 - r ** 2) * df
p_val = stats.f.sf(F, 1, df)

# создаем таблицу как в лекции
ttlinear = pd.DataFrame(data={
    'Estimate': [round(num, 4) for num in [intercept, slope]],
    'Std.Error': [round(num, 4) for num in [sterresty, sterrestx]],
    't value': [round(num, 2) for num in [ty, tx]], 'Pr(>|t|)': [py, px]},
    index=['(Intercept)', 'hs_grand'])

# вычисляем остатки
# residuals = Y - intercept - slope*X
fig, ax1 = plt.subplots(nrows=1, ncols=1, figsize=(10, 7))

# точечный график
ax1.scatter(X, Y)

# регрессионная прямая
x1 = np.linspace(min(X), max(X), 51)
y1 = intercept + slope * x1
plt.plot(x1, y1, '-r', label='b0 = {}, b1 = {}'.format(round(intercept, 2), round(slope, 2)))

plt.grid()
plt.title('Связь бедности и уровня образования')
plt.xlabel('Среднее образование (%)')
plt.ylabel('Бедность (%)')
plt.xticks(np.arange(76, 93, step=4))
plt.yticks(np.arange(5, 18, step=5))
plt.legend(loc='upper right')
plt.show()

print(ttlinear)
print('')
print('Multiple R-squared: {},'.format(round(r ** 2, 4)))
print('F-statistic(1,{}) = {}, p-value = {}'.format(df, round(F, 2), p_val))