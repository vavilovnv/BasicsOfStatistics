# Конспект курса "Основы статистики"

**_Генеральная совокупность_** – множество всех объектов, относительно которых делаются выводы в рамках исследования.

**_Выборка_** – часть генеральной совокупности элементов, которая охватывается экспериментом, наблюдением, опросом.

## Виды выборок:

* Простая случайная выборка (simple random sample)
* Стратифицированная выборка (stratified sample)
* Групповая выборка (claster sample)

## Типы переменных

1. Количественные (numerical) – измеренные значения:
    * Непрерывные ([0; 1]);
    * Дискретные (1, 2,..).
2. Номинативные (categorical) – разделение на группы (1=м, 2=ж).
3. Ранговые (ordinal) – операции сравнения (например, распределение мест в забеге).

## Виды графиков

**_Histogramm (гистограмма)_** – график, показывающий как часто значение переменной встречается на определенном промежутке.

**_Dot plot (точечный график)_** – график, в котором каждой точке соответствует одно значение выборки.

**_Box plot (ящик с усами)_** – график, показывающий медиану, нижний и верхний квартили, минимальное и максимальное значение выборки и выбросы. В ящик попадют значения (50% измерений), лежащих между квантилями <a href="https://www.codecogs.com/eqnedit.php?latex=x_{0,25}" target="_blank"><img src="https://latex.codecogs.com/png.latex?x_{0,25}" title="x_{0,25}" /></a> и <a href="https://www.codecogs.com/eqnedit.php?latex=x_{0.25}" target="_blank"><img src="https://latex.codecogs.com/png.latex?x_{0,25}" title="x_{0.75}" /></a>. Вверх и вниз от ящика исходят два отрезка равные <a href="https://www.codecogs.com/eqnedit.php?latex=1.5&space;*&space;(x_{0,75}&space;-&space;x_{0,25})" target="_blank"><img src="https://latex.codecogs.com/png.latex?1.5&space;*&space;(x_{0,75}&space;-&space;x_{0,25})" title="1.5 * (x_{0,75} - x_{0,25})" /></a>, то есть полтора межквартильных размаха. Точки, превышающие с своем отклонении полтора межквартильных размаха, отображаются отдельно.

**_Q-Q plot (график квантиль-квантиль)_** – показывает насколько выборочное значение соответствует нормальному распределению, линия – идеальное нормальное распределение.

**_Scatter plot (диаграмма рассеяния)_** – диагрмма, изображающая значения двух переменных в виде точек на декартовой плоскости.

**_Biplot_** – график первых двух компонент с вкладом каждой переменной.

## Меры центральной тенденции

**_Мода (mode)_** – значение признака, котороые встречается максимально часто.

**_Медиана (median)_** – значение признака, которое делит упорядоченное множество данных пополам.

**_Среднее значение (mean)_** – сумма всех значений признака, деленная на количество измеренных значений.

Обозначения: <a href="https://www.codecogs.com/eqnedit.php?latex=M_{x}" target="_blank"><img src="https://latex.codecogs.com/png.latex?M_{x}" title="M_{x}" /></a> – среднее значение генеральной совокупности, <a href="https://www.codecogs.com/eqnedit.php?latex=\overline{X}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\overline{X}" title="\overline{X}" /></a> – среднее значение выборки.

Свойста среднего:

1. <a href="https://www.codecogs.com/eqnedit.php?latex=M_{x}&space;=&space;\frac{1}{n}\sum&space;x_{i}" target="_blank"><img src="https://latex.codecogs.com/png.latex?M_{x}&space;=&space;\frac{1}{n}\sum&space;x_{i}" title="M_{x} = \frac{1}{n}\sum x_{i}" /></a>
2. <a href="https://www.codecogs.com/eqnedit.php?latex=M_{x&space;&plus;&space;C}&space;=&space;M_{x}&space;&plus;&space;C" target="_blank"><img src="https://latex.codecogs.com/png.latex?M_{x&space;&plus;&space;C}&space;=&space;M_{x}&space;&plus;&space;C" title="M_{x + C} = M_{x} + C" /></a>
3. <a href="https://www.codecogs.com/eqnedit.php?latex=M_{x&space;*&space;C}&space;=&space;M_{x}&space;*&space;C" target="_blank"><img src="https://latex.codecogs.com/png.latex?M_{x&space;*&space;C}&space;=&space;M_{x}&space;*&space;C" title="M_{x * C} = M_{x} * C" /></a>
4. <a href="https://www.codecogs.com/eqnedit.php?latex=\sum&space;(x_{i}&space;-&space;M_{x})&space;=&space;0" target="_blank"><img src="https://latex.codecogs.com/png.latex?\sum&space;(x_{i}&space;-&space;M_{x})&space;=&space;0" title="\sum (x_{i} - M_{x}) = 0" /></a>


## Меры изменчивости

**_Размах (range)_** – разность максимального и минимального значения.

**_Дисперсия (variance)_** – средний квадрат отклонений индивидуальных значений признака от их средней величины.

**_Среднеквадратическое отклонение (standard deviation, стандартное отклонение)_** – среднее отклонение индивидуальных значений признака от их средней величины.

Обозначения: <a href="https://www.codecogs.com/eqnedit.php?latex=D_{x}" target="_blank"><img src="https://latex.codecogs.com/png.latex?D_{x}" title="D_{x}" /></a> – дисперсия генеральной совокупности, <a href="https://www.codecogs.com/eqnedit.php?latex=\sigma" target="_blank"><img src="https://latex.codecogs.com/png.latex?\sigma" title="\sigma" /></a> – стандартное отклонение генеральной совокупности, <a href="https://www.codecogs.com/eqnedit.php?latex=sd_{x}" target="_blank"><img src="https://latex.codecogs.com/png.latex?sd_{x}" title="sd_{x}" /></a> – стандартное отклонение выборки.

Свойства дисперсии и стандартного отклонения:
1. <a href="https://www.codecogs.com/eqnedit.php?latex=D_{x}&space;=&space;\frac{1}{n&space;-&space;1}\sum&space;(x_{i}&space;-&space;\overline{x})^{2}" target="_blank"><img src="https://latex.codecogs.com/png.latex?D_{x}&space;=&space;\frac{1}{n&space;-&space;1}\sum&space;(x_{i}&space;-&space;\overline{x})^{2}" title="D_{x} = \frac{1}{n - 1}\sum (x_{i} - \overline{x})^{2}" /></a>
2. <a href="https://www.codecogs.com/eqnedit.php?latex=D_{x&space;&plus;&space;C}&space;=&space;D_{x},&space;sd_{x&space;&plus;&space;C}&space;=&space;sd_{x}" target="_blank"><img src="https://latex.codecogs.com/png.latex?D_{x&space;&plus;&space;C}&space;=&space;D_{x},&space;sd_{x&space;&plus;&space;C}&space;=&space;sd_{x}" title="D_{x + C} = D_{x}, sd_{x + C} = sd_{x}" /></a>
3. <a href="https://www.codecogs.com/eqnedit.php?latex=D_{x&space;*&space;C}&space;=&space;D_{x}&space;*&space;C^{2},&space;sd_{x&space;*&space;C}&space;=&space;sd_{x}&space;*&space;C" target="_blank"><img src="https://latex.codecogs.com/png.latex?D_{x&space;*&space;C}&space;=&space;D_{x}&space;*&space;C^{2},&space;sd_{x&space;*&space;C}&space;=&space;sd_{x}&space;*&space;C" title="D_{x * C} = D_{x} * C^{2}, sd_{x * C} = sd_{x} * C" /></a> 


## Квантили распределения

**_Квантиль_** – значение, которое заданная случайная величина не превышает с фиксированной вероятностью: <a href="https://www.codecogs.com/eqnedit.php?latex=P(X\leq&space;x_{\alpha&space;})\geq&space;\alpha" target="_blank"><img src="https://latex.codecogs.com/png.latex?P(X\leq&space;x_{\alpha&space;})\geq&space;\alpha" title="P(X\leq x_{\alpha })\geq \alpha" /></a>.

**_Квартили_** – три значения признака, которые делят упорядоченное множество данных на четыре равные части.

**_Межквартильный размах_** – разница между третьим и первым квартилем. Характеризует вариантивность изучаемого признака.

## Нормальное распределение

**_Нормальное распределение_** – унимодально, симметрично, отконения наблюдений от среднего подчиняются определенному вероятностному закону (правило <a href="https://www.codecogs.com/eqnedit.php?latex=2\sigma" target="_blank"><img src="https://latex.codecogs.com/png.latex?2\sigma" title="2\sigma" /></a> и <a href="https://www.codecogs.com/eqnedit.php?latex=3\sigma" target="_blank"><img src="https://latex.codecogs.com/png.latex?3\sigma" title="3\sigma" /></a>):
1. <a href="https://www.codecogs.com/eqnedit.php?latex=P(\overline{x}&space;-&space;\sigma&space;<&space;X&space;<&space;\overline{x}&space;&plus;&space;\sigma)&space;=&space;0.68" target="_blank"><img src="https://latex.codecogs.com/png.latex?P(\overline{x}&space;-&space;\sigma&space;<&space;X&space;<&space;\overline{x}&space;&plus;&space;\sigma)&space;=&space;0.68" title="P(\overline{x} - \sigma < X < \overline{x} + \sigma) = 0.68" /></a>
2. <a href="https://www.codecogs.com/eqnedit.php?latex=P(\overline{x}&space;-&space;2\sigma&space;<&space;X&space;<&space;\overline{x}&space;&plus;&space;2\sigma)&space;=&space;0.95" target="_blank"><img src="https://latex.codecogs.com/png.latex?P(\overline{x}&space;-&space;2\sigma&space;<&space;X&space;<&space;\overline{x}&space;&plus;&space;2\sigma)&space;=&space;0.95" title="P(\overline{x} - 2\sigma < X < \overline{x} + 2\sigma) = 0.95" /></a>
3. <a href="https://www.codecogs.com/eqnedit.php?latex=P(\overline{x}&space;-&space;3\sigma&space;<&space;X&space;<&space;\overline{x}&space;&plus;&space;3\sigma)&space;=&space;0.98" target="_blank"><img src="https://latex.codecogs.com/png.latex?P(\overline{x}&space;-&space;3\sigma&space;<&space;X&space;<&space;\overline{x}&space;&plus;&space;3\sigma)&space;=&space;0.98" title="P(\overline{x} - 3\sigma < X < \overline{x} + 3\sigma) = 0.98" /></a>

**_Стандартизация (Z-преобразование)_** – преобразование полученных данных в стандартную Z-шкалу (Z-scores) со средним <a href="https://www.codecogs.com/eqnedit.php?latex=M_{z}&space;=&space;0,&space;D_{z}&space;=&space;1" target="_blank"><img src="https://latex.codecogs.com/png.latex?M_{z}&space;=&space;0,&space;D_{z}&space;=&space;1" title="M_{z} = 0, D_{z} = 1" /></a>:

<a href="https://www.codecogs.com/eqnedit.php?latex=z_{i}&space;=&space;\frac{x_{i}&space;-&space;\overline{X}}{sd_{x}}" target="_blank"><img src="https://latex.codecogs.com/png.latex?z_{i}&space;=&space;\frac{x_{i}&space;-&space;\overline{X}}{sd_{x}}" title="z_{i} = \frac{x_{i} - \overline{X}}{sd_{x}}" /></a>
