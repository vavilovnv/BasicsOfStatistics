# https://stepik.org/lesson/8090/step/2?unit=1369
# Интерпретация результатов регрессионного анализа с несколькими независимыми переменными

import pandas as pd, numpy as np, seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv('http://d396qusza40orc.cloudfront.net/statistics/lec_resources/states.csv')

data_crop = data[['white', 'hs_grad', 'poverty']]
data_crop.head()
white, hs_grad, poverty = [column for column in data_crop.values.T]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs=white, ys=poverty, zs=hs_grad)

ax.set_xlabel('White(%)')
ax.set_ylabel('Poverty(%)')
ax.set_zlabel('Higher education(%)')
plt.show()
