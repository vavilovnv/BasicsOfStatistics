# Страницы темы: https://stepik.org/lesson/9294/step/4?discussion=132848&reply=3465540&unit=1827

# Визуализация box plot

import numpy as np
import matplotlib.pyplot as plt

data_to_plot = np.array([157,159,161,164,165,166,167,167,167,168,169,170,170,170,
                         171,171,172,172,172,172,173,173,175,175,177,178,178,179,185])
plt.figure(1,figsize=(5,6))
plt.subplot(111)
plt.axis([0,2,155,190])
plt.boxplot(data_to_plot, showfliers=True)
plt.show()
