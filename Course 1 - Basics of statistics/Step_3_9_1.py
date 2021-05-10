# https://stepik.org/lesson/9995/step/2?discussion=1178182&reply=3790608&unit=1925
# Визуализация корреляции независимых переменных и выбор лучшей модели

import pandas as pd, numpy as np, seaborn as sns
import matplotlib.pyplot as plt


# Расчет коэфф. корреляции между двумя массивами
def corr(x, y, **kwargs):
    # расчет значения
    coef = np.corrcoef(x, y)[0][1]
    # описание обозначения
    label = r'$\rho$ = ' + str(round(coef, 2))
    # добавление обозначения на график
    ax = plt.gca()
    ax.annotate(label, xy=(0.2, 0.45), size=20, xycoords=ax.transAxes)


df = pd.read_csv('http://d396qusza40orc.cloudfront.net/statistics/lec_resources/states.csv')

g = sns.PairGrid(df, diag_sharey=False)
g.map_upper(corr) # коэфф. корреляции
g.map_lower(sns.scatterplot) # множества значений
g.map_diag(sns.kdeplot) # графики
plt.show()
