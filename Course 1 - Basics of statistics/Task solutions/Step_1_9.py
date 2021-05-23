# Страницы темы: https://stepik.org/lesson/8079/step/8?unit=1359

# Рассчитайте 99% доверительный интервал для следующего примера:
# X = 10
# sd = 5
# n = 100

import math
from scipy import stats

def confidence_interval(sd, X, n, target_interval):
    z = abs(stats.norm.ppf((1 - target_interval)/2))
    se = sd / math.sqrt(n)
    return (round(X - z * se,  2),  round(X + z * se,  2))

print(confidence_interval(5, 10, 100, 0.99))