# Страницы темы: https://stepik.org/lesson/9166/step/10?unit=1828

# Правило "двух" и "трех" сигм

import scipy.stats as st

# данные для примера
point = 154 # значение признака
mean = 150 # среднее значение
std = 8 # стандартное отклонение

z = (point - mean) / std # z-значение для признака
if point > mean:
    probability = (1 - st.norm.cdf(z))
else:
    probability = (st.norm.cdf(z))
print(f'{round(probability*100, 2)} %')