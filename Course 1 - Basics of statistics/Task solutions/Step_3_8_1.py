# https://stepik.org/lesson/8090/step/2?unit=1369
# Интерпретация результатов регрессионного анализа с несколькими независимыми переменными

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('http://d396qusza40orc.cloudfront.net/statistics/lec_resources/states.csv')

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(xs=data.white, ys=data.poverty, zs=data.hs_grad)
ax.set_xlabel('White(%)')
ax.set_ylabel('Poverty(%)')
ax.set_zlabel('Higher education(%)')
plt.show()
