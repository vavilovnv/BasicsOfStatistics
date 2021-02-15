# Страницы темы: https://stepik.org/lesson/9166/step/12?unit=1828

# Считается, что значение IQ (уровень интеллекта) у людей имеет нормальное распределение со средним значением равным 100
# и стандартным отклонением равным 15 (M = 100, sd = 15).
# Какой приблизительно процент людей обладает IQ > 125?

import random

probability, M, sd, x = 0, 100, 15, 125
for i in range(100000):
    if random.normalvariate(M, sd) > x:
        probability += 1
print(f'{probability * 0.001} %')