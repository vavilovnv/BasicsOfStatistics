# https://stepik.org/lesson/8086/step/11?unit=1365
# Визуализация корреляции

from scipy import stats
import matplotlib.pyplot as plt
import numpy as np


def cortest(corr, lenX):
    t = corr[0] * ((len(X) - 2) / (1 - corr[0] ** 2)) ** 0.5  # t value
    print('data: x and y')
    print(f't = {round(t, 5)}, df = {len(X) - 2}, p-value = {round(stats.t.sf(np.abs(t), 48) * 2, 5)}')

    # Use the Fisher transformation to get z
    z = np.arctanh(corr[0])
    print(f'z value: {z}')

    # Sigma value as standard error
    sigma = (1 / ((len(X) - 3) ** 0.5))
    print('sigma value: {sigma}')

    # Get normal 95% interval probability density function for normal continuous random variable apply two-sided
    # conditional formula
    cint = z + np.array([-1, 1]) * sigma * stats.norm.ppf((1 + 0.95) / 2)

    # Finally take hyperbolic tangent to get interval values for 95%
    interval = np.tanh(cint)

    if corr != 0:
        print('alternative hypothesis: true correlation is not equal to 0')
    print('95 percent confidence interval:', interval)
    print('sample estimates:')
    print('cor', corr[0])


# вычисляем корреляцию
X = stats.norm.rvs(loc=0, scale=1, size=50)
Y = stats.norm.rvs(loc=0, scale=1, size=50)
corr = stats.pearsonr(X, Y)

# строим scatter plot
plt.scatter(X, Y)
plt.grid()
plt.show()

print('correlation: {corr}')

cortest((0.2858888,), 50)
