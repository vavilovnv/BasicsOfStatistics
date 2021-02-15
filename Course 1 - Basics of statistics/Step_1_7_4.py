# Страницы темы: https://stepik.org/lesson/9166/step/13?unit=1828

# Считается, что значение IQ (уровень интеллекта) у людей имеет нормальное распределение со средним значением равным 100
# и стандартным отклонением равным 15 (M = 100, sd = 15).
# Какой приблизительно процент людей обладает IQ  на промежутке от 70 до 112?

import random

probability, M, sd, x = 0, 100, 15, [70, 112]
p = [True if x[0] < random.normalvariate(M, sd) < x[1] else False for i in range(100000)]
print(f'{round(p.count(True) * 0.001)}%')