# Конспект курса "Основы статистики"

**_Генеральная совокупность_** – множество всех объектов, относительно которых делаются выводы в рамках исследования.

**_Выборка_** – часть генеральной совокупности элементов, которая охватывается экспериментом, наблюдением, опросом.

## Все условные обозначения встречаемые по тексту ниже  
<a href="https://www.codecogs.com/eqnedit.php?latex=M_{x}" target="_blank"><img src="https://latex.codecogs.com/png.latex?M_{x}" title="M_{x}" /></a> – среднее значение генеральной совокупности  
<a href="https://www.codecogs.com/eqnedit.php?latex=\overline{X}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\overline{X}" title="\overline{X}" /></a> – среднее значение выборки  
<a href="https://www.codecogs.com/eqnedit.php?latex=D_{x}" target="_blank"><img src="https://latex.codecogs.com/png.latex?D_{x}" title="D_{x}" /></a> – дисперсия генеральной совокупности  
<a href="https://www.codecogs.com/eqnedit.php?latex=\sigma" target="_blank"><img src="https://latex.codecogs.com/png.latex?\sigma" title="\sigma" /></a> – стандартное отклонение генеральной совокупности  
*df* - число степеней свободы  
<a href="https://www.codecogs.com/eqnedit.php?latex=sd_{x}" target="_blank"><img src="https://latex.codecogs.com/png.latex?sd_{x}" title="sd_{x}" /></a> – стандартное отклонение выборки  
<a href="https://www.codecogs.com/eqnedit.php?latex=se" target="_blank"><img src="https://latex.codecogs.com/gif.latex?se" title="se" /></a> - стандартная ошибка среднего


## Виды выборок

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

**_Box plot (ящик с усами)_** – график, показывающий медиану, нижний и верхний квартили, минимальное и максимальное значение выборки и выбросы. В ящик попадют значения (50% измерений), лежащих между квантилями <a href="https://www.codecogs.com/eqnedit.php?latex=x_{0,25}" target="_blank"><img src="https://latex.codecogs.com/png.latex?x_{0,25}" title="x_{0,25}" /></a> и <a href="https://www.codecogs.com/eqnedit.php?latex=x_{0.25}" target="_blank"><img src="https://latex.codecogs.com/png.latex?x_{0,75}" title="x_{0.75}" /></a>. Вверх и вниз от ящика исходят два отрезка равные <a href="https://www.codecogs.com/eqnedit.php?latex=1.5&space;*&space;(x_{0,75}&space;-&space;x_{0,25})" target="_blank"><img src="https://latex.codecogs.com/png.latex?1.5&space;*&space;(x_{0,75}&space;-&space;x_{0,25})" title="1.5 * (x_{0,75} - x_{0,25})" /></a>, то есть полтора межквартильных размаха. Точки, превышающие в своем отклонении полтора межквартильных размаха, отображаются отдельно.

**_Q-Q plot (график квантиль-квантиль)_** – показывает насколько выборочное значение соответствует нормальному распределению. Линия – идеальное нормальное распределение.

**_Scatter plot (диаграмма рассеяния)_** – диагрмма, изображающая значения двух переменных в виде точек на декартовой плоскости.

**_Biplot_** – график первых двух компонент с вкладом каждой переменной.

## Меры центральной тенденции

**_Мода (mode)_** – значение признака, который встречается максимально часто.

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

## Центральная предельная теорема

**_Стандартная ошибка среднего_** - стандартное отклонение симметричного распределения выборочных средних вокруг среднего значения генеральной совокупности при многократном повторении эксперимента: 

<a href="https://www.codecogs.com/eqnedit.php?latex=se_{x}&space;=&space;\frac{\sigma&space;}{\sqrt{n}}&space;=&space;\frac{sd_{x}}{\sqrt{n}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?se_{x}&space;=&space;\frac{\sigma&space;}{\sqrt{n}}&space;=&space;\frac{sd_{x}}{\sqrt{n}}" title="se_{x} = \frac{\sigma }{\sqrt{n}} = \frac{sd_{x}}{\sqrt{n}}" /></a> при _n_ > 30.

## Доверительный интервал для среднего

<a href="https://www.codecogs.com/eqnedit.php?latex=\left&space;[&space;\mu&space;-&space;1.96\sigma,&space;\mu&space;&plus;&space;1.96\sigma&space;\right]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\left&space;[&space;\mu&space;-&space;1.96\sigma,&space;\mu&space;&plus;&space;1.96\sigma&space;\right]" title="\left [ \mu - 1.96\sigma, \mu + 1.96\sigma \right]" /></a> – 95% попадание среднего генеральной совокупности <a href="https://www.codecogs.com/eqnedit.php?latex=\mu" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mu" title="\mu" /></a> в данный интервал (из всех выборочных средних).

<a href="https://www.codecogs.com/eqnedit.php?latex=\left&space;[&space;\mu&space;-&space;2.58\sigma,&space;\mu&space;&plus;&space;2.58\sigma&space;\right]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\left&space;[&space;\mu&space;-&space;2.58\sigma,&space;\mu&space;&plus;&space;2.58\sigma&space;\right]" title="\left [ \mu - 2.58\sigma, \mu + 2.58\sigma \right]" /></a> – 99% доверительный интервал.


## Идея статистического вывода

**_Нулевая гипотеза_** <a href="https://www.codecogs.com/eqnedit.php?latex=H_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_{0}" title="H_{0}" /></a> – отсутствие значимых различий между средним значением выборки и средним значением генеральной совокупности.  
Дополнительная интерпретация: ошибка первого рода - считаем нулевую гипотезу **неверной**, когда она является **верной**. Ошибка второго рода - считаем нулевую гипотезу **верной**, когда она является **неверной**.

**_Альтернативная гипотеза_** <a href="https://www.codecogs.com/eqnedit.php?latex=H_{1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_{1}" title="H_{1}" /></a> – значимое отклонение между средним значением выборки и средним значением генеральной совокупности.

<a href="https://www.codecogs.com/eqnedit.php?latex=\rho" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\rho" title="\rho" /></a>**_-уровень значимости_** – вероятность получения такого или еще более сильного отклонения от среднего значения, если верна <a href="https://www.codecogs.com/eqnedit.php?latex=H_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_{0}" title="H_{0}" /></a>. Чем меньше <a href="https://www.codecogs.com/eqnedit.php?latex=\rho" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\rho" title="\rho" /></a>, тем больше оснований отклонить нулевую гипотезу. Обычно при <a href="https://www.codecogs.com/eqnedit.php?latex=\rho" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\rho" title="\rho" /></a> < 0.05 принимаем <a href="https://www.codecogs.com/eqnedit.php?latex=H_{1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_{1}" title="H_{1}" /></a>, т.е. мы получили статистически значимое отклонение.

**_Ошибка 1 типа_** – приняли альтернативную гипотезу, хотя верна нулевая.

**_Ошибка 2 типа_** – приняли нулевую гипотезу, хотя верна альтернативная.


## Распределение Стьюдента

Если число наблюдений невелико (n < 30) и <a href="https://www.codecogs.com/eqnedit.php?latex=\sigma" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sigma" title="\sigma" /></a> неизвестно, то используется **_распределение Стьюдента_** (t-distribution): унимодально, симметрично, но наблюдения с большей вероятностью попадают за пределы <a href="https://www.codecogs.com/eqnedit.php?latex=\pm&space;2\sigma" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\pm&space;2\sigma" title="\pm 2\sigma" /></a> от среднего значения <a href="https://www.codecogs.com/eqnedit.php?latex=\mu" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mu" title="\mu" /></a>, чем при нормальном распределении.

Форма распределения определяется числом **_степеней свободы_** (_df = n - 1_, degrees of freedom), c увелечением _df_ распределение стремится к нормальному.

**Критерий Стьюдента**

<a href="https://www.codecogs.com/eqnedit.php?latex=H_{0}:M_{1}&space;=&space;M_{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_{0}:M_{1}&space;=&space;M_{2}" title="H_{0}:M_{1} = M_{2}" /></a>   <a href="https://www.codecogs.com/eqnedit.php?latex=H_{0}:M_{1}&space;\neq&space;M_{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_{0}:M_{1}&space;\neq&space;M_{2}" title="H_{0}:M_{1} \neq M_{2}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=X_{1}&space;-&space;X_{2}&space;\in&space;t&space;(df&space;=&space;n_{1}&space;&plus;&space;n_{2}&space;-&space;2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?X_{1}&space;-&space;X_{2}&space;\in&space;t&space;(df&space;=&space;n_{1}&space;&plus;&space;n_{2}&space;-&space;2)" title="X_{1} - X_{2} \in t (df = n_{1} + n_{2} - 2)" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=se&space;=&space;\sqrt{\frac{sd_{1}^{2}}{n_{1}}&space;&plus;&space;\frac{sd_{2}^{2}}{n_{2}}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?se&space;=&space;\sqrt{\frac{sd_{1}^{2}}{n_{1}}&space;&plus;&space;\frac{sd_{2}^{2}}{n_{2}}}" title="se = \sqrt{\frac{sd_{1}^{2}}{n_{1}} + \frac{sd_{2}^{2}}{n_{2}}}" /></a>, <a href="https://www.codecogs.com/eqnedit.php?latex=t&space;=&space;\frac{\overline{X_{1}}&space;-&space;\overline{X_{2}}}{se}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?t&space;=&space;\frac{\overline{X_{1}}&space;-&space;\overline{X_{2}}}{se}" title="t = \frac{\overline{X_{1}} - \overline{X_{2}}}{se}" /></a>

Зная число степеней свободы и _t_-значение, мы можем расчитать _p_-уровень значимости.

**Применимость критерия Стьюдента:**

1. Гомогенность дисперсий (приблизительно одинаковы), можно проверить используя критерий Левена или критерий Фишера.
2. Нормальность распределения при _n_ < 30.

**Проверка на нормальность**

* **Тест Колмагорова-Смирнова** и **критерий Шапиро-Уилка**: если получаем _p_-уровень значимости больше 0.05, значит наша выборка значимо не отличается от нормальной.

* **Критерий Манна-Уитни** переходит к ранжированным значениям и может быть использован при наличии значительных выбросов в выборке.

## Дисперсионный анализ
*ANOVA, ANalysis Of VAriance* – позволяет сранивать среднее значение трех и более групп.  
<a href="https://www.codecogs.com/eqnedit.php?latex=H_{0}:M_{1}&space;=&space;M_{2}&space;=&space;M_{3}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_{0}:M_{1}&space;=&space;M_{2}&space;=&space;M_{3}" title="H_{0}:M_{1} = M_{2} = M_{3}" /></a>  <a href="https://www.codecogs.com/eqnedit.php?latex=H_{0}:!(M_{1}&space;=&space;M_{2}&space;=&space;M_{3})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_{0}:!(M_{1}&space;=&space;M_{2}&space;=&space;M_{3})" title="H_{0}:!(M_{1} = M_{2} = M_{3})" /></a>  
Мы говорим, что вся изменчивость наших данных без разделения на группы *SST* (Total Sum of Squares - общая сумма квадратов) может быть обусловлена изменчивостью внутри групп *SSW* (Sum of Squares Within groups - сумма квадратов внутригрупповая) и изменчивостью между группами *SSB* (Sum of Squares Between groups - cумма квадратов межгрупповая).

Если *SSB* ≫ *SSW*, то весьма вероятно что как минимум два средних значения отличаются друг от друга. Основной статистический показатель – критерий Фишера:  
<a href="https://www.codecogs.com/eqnedit.php?latex=F&space;=&space;\frac{SSB}{m-1}&space;/&space;\frac{SSW}{n-m}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F&space;=&space;\frac{SSB}{m-1}&space;/&space;\frac{SSW}{n-m}" title="F = \frac{SSB}{m-1} / \frac{SSW}{n-m}" /></a>  
где  *n* – размер выборки, *m* – количество групп.

**Поправка Бонферрони**

*Bonferroni correction* – при увелечении количества групп, необходима корректировка значения *p*-уровня значимости. Необходимо *p*-уровень значимости разделить на количество парных сравнений в эксперименте: <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{m(m-1)}{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{m(m-1)}{2}" title="\frac{m(m-1)}{2}" /></a>.

**Критерий Тьюки**

*Tukey HSD* – расчитываются доверительные интервалы разности между средними значениями групп. Является менее консервативным, чем поправка Бонферрони.

## Многофакторный дисперсионный анализ

*MANOVA, Multivariate analysis of variance* – позволяет сранивать среднее значение трех и более групп в зависимости от нескольких переменных. Вся изменчивость обусловлена:  
<a href="https://www.codecogs.com/eqnedit.php?latex=SST&space;=&space;SSW&space;&plus;&space;SSB_{A}&space;&plus;&space;SSB_{B}&space;&plus;&space;SSB_{A}&space;*&space;SSB_{B}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?SST&space;=&space;SSW&space;&plus;&space;SSB_{A}&space;&plus;&space;SSB_{B}&space;&plus;&space;SSB_{A}&space;*&space;SSB_{B}" title="SST = SSW + SSB_{A} + SSB_{B} + SSB_{A} * SSB_{B}" /></a>

## Корреляция

**_Коэффициент ковариации_** – мера линейной зависимости двух переменных:  
<a href="https://www.codecogs.com/eqnedit.php?latex=cov_{XY}&space;=&space;\frac{\sum_{i}^{}(x_{i}&space;-&space;\overline{X})&space;*&space;(y_{i}&space;-&space;\overline{Y})}{N&space;-&space;1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?cov_{XY}&space;=&space;\frac{\sum_{i}^{}(x_{i}&space;-&space;\overline{X})&space;*&space;(y_{i}&space;-&space;\overline{Y})}{N&space;-&space;1}" title="cov_{XY} = \frac{\sum_{i}^{}(x_{i} - \overline{X}) * (y_{i} - \overline{Y})}{N - 1}" /></a>

**_Коэффициент корреляции Пирсона_** – показатель силы и направления взаимосвязи двух количественных переменных, знак показывает направление взаимосвязи:  
<a href="https://www.codecogs.com/eqnedit.php?latex=r_{XY}&space;=&space;\frac{cov_{XY}}{\sigma_{X}\cdot\sigma_{Y}}&space;\in&space;[-1;&space;1]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_{XY}&space;=&space;\frac{cov_{XY}}{\sigma_{X}\cdot\sigma_{Y}}&space;\in&space;[-1;&space;1]" title="r_{XY} = \frac{cov_{XY}}{\sigma_{X}\cdot\sigma_{Y}} \in [-1; 1]" /></a>

**_Коэффициент детерминации_** <a href="https://www.codecogs.com/eqnedit.php?latex=R^{2}&space;=&space;(r_{XY})^{2}&space;\in&space;[0;&space;1]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?R^{2}&space;=&space;(r_{XY})^{2}&space;\in&space;[0;&space;1]" title="R^{2} = (r_{XY})^{2} \in [0; 1]" /></a> – показывает в какой степени дисперсия одной переменной обусловлена влиянием другой переменной.

**Особенности корреляции:**

* Коэффициент корреляции применим если взаимосвязь линейна и монотонна, а также при отсутствии значительных выбросов (иначе необходимо использовать непараметрические аналоги).
* Положительная или отрицательная корреляция не говорит о причинно-следственной зависимости между переменными.
* Корреляция между двумя переменными может обуславливаться существованием третьей переменной, влияющей на обе эти переменные.

**Непараметрические аналоги коэффициента корреляции Пирсона**

Коффициенты корреляции Спирмана и Кендалла, так же как и критерий Манна-Уитни, переходят от реальных значений переменных к ранжированным значениям.

## Регрессионный анализ

Одномерный регрессионный анализ применяется для исследования взаимосвязи двух количественных переменных (независимая переменная –  предиктор и зависимая переменная –  критериальная). Изучает как одна переменная определяет или позваляет предсказать другую переменную.

**Линия регрессии**

Линия тренда задается уравнением <a href="https://www.codecogs.com/eqnedit.php?latex=y&space;=&space;b_{0}&space;&plus;&space;b_{1}x" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y&space;=&space;b_{0}&space;&plus;&space;b_{1}x" title="y = b_{0} + b_{1}x" /></a>, где <a href="https://www.codecogs.com/eqnedit.php?latex=b_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?b_{0}" title="b_{0}" /></a> – свободный член (intercept), который отвечает за значение *y*, где линия пересечет ось Y; <a href="https://www.codecogs.com/eqnedit.php?latex=b_{1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?b_{1}" title="b_{1}" /></a> – угловой коэффицент (slope).

Необходимо подобрать <a href="https://www.codecogs.com/eqnedit.php?latex=b_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?b_{0}" title="b_{0}" /></a> и <a href="https://www.codecogs.com/eqnedit.php?latex=b_{1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?b_{1}" title="b_{1}" /></a> так, чтобы линия максимально адекватно отображала связь данных переменных, при этом выдвигается гипотеза <a href="https://www.codecogs.com/eqnedit.php?latex=H_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_{0}" title="H_{0}" /></a>: <a href="https://www.codecogs.com/eqnedit.php?latex=b_{0}&space;=&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?b_{0}&space;=&space;0" title="b_{0} = 0" /></a>.

**Метод наименьших квадратов**

Метод нахождения оптимальных параметров линейной регресии, таких, что сумма квадратов ошибок (остатков) была минимальна. Остаток – расстояние от реального значения до предсказаннного значения, лежащего на прямой (линии регрессии).  
<a href="https://www.codecogs.com/eqnedit.php?latex=b_{1}&space;=&space;\frac{sd_{Y}}{sd_{X}}\cdot&space;r_{XY}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?b_{1}&space;=&space;\frac{sd_{Y}}{sd_{X}}\cdot&space;r_{XY}" title="b_{1} = \frac{sd_{Y}}{sd_{X}}\cdot r_{XY}" /></a>  
<a href="https://www.codecogs.com/eqnedit.php?latex=b_{0}&space;=&space;\overline{Y}&space;-&space;b_{1}&space;\cdot&space;\overline{X}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?b_{0}&space;=&space;\overline{Y}&space;-&space;b_{1}&space;\cdot&space;\overline{X}" title="b_{0} = \overline{Y} - b_{1} \cdot \overline{X}" /></a>

**_Коэффициент детерминации_** – доля дисперсии зависимой переменной _Y_, объясняемая регресионной моделью:  
<a href="https://www.codecogs.com/eqnedit.php?latex=R^{2}&space;=&space;1&space;-&space;\frac{SS_{res}}{SS_{total}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?R^{2}&space;=&space;1&space;-&space;\frac{SS_{res}}{SS_{total}}" title="R^{2} = 1 - \frac{SS_{res}}{SS_{total}}" /></a>  
где <a href="https://www.codecogs.com/eqnedit.php?latex=SS_{res}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?SS_{res}" title="SS_{res}" /></a> (residuals) - сумма квадратов остатков (расстояний до регрессионой прямой), а <a href="https://www.codecogs.com/eqnedit.php?latex=SS_{total}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?SS_{total}" title="SS_{total}" /></a> - общая изменчивость (сумма квадратов расстояний до прямой <a href="https://www.codecogs.com/eqnedit.php?latex=y&space;=&space;\overline{Y}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y&space;=&space;\overline{Y}" title="y = \overline{Y}" /></a>). Таким образом, <a href="https://www.codecogs.com/eqnedit.php?latex=R^{2}&space;\approx&space;1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?R^{2}&space;\approx&space;1" title="R^{2} \approx 1" /></a> означает, что почти вся изменчивость переменной объясняется нашей регрессионной моделью.

**Условия применимости:**

1. Линейная взаимосвязь *X* и *Y*.  
Если зависимость на самом деле нелинейна, то предсказание будет ошибочно. Пути ликвидации нелинейности:
    * Трансформация Тьюки (Tukey Ladder of Powers) – возведение *X* в степень, теряется интерпретируемость.
    * Логарифмическая трансформация (Log transformation) – взятие логарифма от *X* и/или *Y*, интерпретируемость коэффициента наклона <a href="https://www.codecogs.com/eqnedit.php?latex=b_{1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?b_{1}" title="b_{1}" /></a>:  
    a) <a href="https://www.codecogs.com/eqnedit.php?latex=log&space;Y&space;=&space;b_{0}&space;&plus;&space;b_{1}&space;\cdot&space;log&space;X" target="_blank"><img src="https://latex.codecogs.com/gif.latex?log&space;Y&space;=&space;b_{0}&space;&plus;&space;b_{1}&space;\cdot&space;log&space;X" title="log Y = b_{0} + b_{1} \cdot log X" /></a> - на сколько процентов увеличится значение зависимой переменной при изменении зависимой переменной на один процент.  
    b) <a href="https://www.codecogs.com/eqnedit.php?latex=log&space;Y&space;=&space;b_{0}&space;&plus;&space;b_{1}&space;\cdot&space;X" target="_blank"><img src="https://latex.codecogs.com/gif.latex?log&space;Y&space;=&space;b_{0}&space;&plus;&space;b_{1}&space;\cdot&space;X" title="log Y = b_{0} + b_{1} \cdot X" /></a> – при единичном изменении переменной *X*, переменная *Y* в среднем изменяется на <a href="https://www.codecogs.com/eqnedit.php?latex=100&space;\cdot&space;b_{1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?100&space;\cdot&space;b_{1}" title="100 \cdot b_{1}" /></a> процентов.  
    c) <a href="https://www.codecogs.com/eqnedit.php?latex=Y&space;=&space;b_{0}&space;&plus;&space;b_{1}&space;\cdot&space;log&space;X" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Y&space;=&space;b_{0}&space;&plus;&space;b_{1}&space;\cdot&space;log&space;X" title="Y = b_{0} + b_{1} \cdot log X" /></a>– изменение на 1% по *X* в среднем приводит к <a href="https://www.codecogs.com/eqnedit.php?latex=0.01&space;\cdot&space;b_{1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?0.01&space;\cdot&space;b_{1}" title="0.01 \cdot b_{1}" /></a> изменению по переменной *Y*.
    * Трансформация Бокса-Кокса (Box-Cox transformation) – обычно используется для трансформации зависимой переменной в случае, если у нас есть ненормальное распределение ошибок и/или нелинейность взаимосвязи, а также в случае гетероскедастичности.
2. Независимость наблюдений.  
    Источники:  
    * Повторные измерения (на разных уровнях независимой переменной): снижение чувствительности теста, искуственное увелечение мощности теста (псевдореплекация).  
    * Повторные пробы (на одном и том же уровне независимой переменной): искажение результатов.  
    * Кластеризация данных (нет повторных измерений, но данные взяты из нескольких гомогенных групп): искажение результатов.
3. Независимость предикторов. Отсутствие мультиколлинеарности – линейной зависимости между предикорами.
    * Абсолютная мультиколлинеарность – корреляция между двумя предикторами равна <a href="https://www.codecogs.com/eqnedit.php?latex=\pm&space;1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\pm&space;1" title="\pm 1" /></a>.  
    * Если мы хотим только предсказывать значения, то мультиколлинеарность не проблема.
    * Для выявления можно построить корреляционную матрицу.
    * VIF (Variance Inflation Factor) – показывает, насколько хорошо предиктор объясняется другими предикторами. Если *VIF > 10*, то предиктор лучше исключить из модели. Квадратный корень из *VIF* показывает, во сколько раз стала больше стандартная ошибка данного коэффициента, по сравнению с ситуацией, если он был независим от других предикторов.
4. Нормальное распределение остатков.
5. Гомоскедастичность – постоянная изменчивость остатков на всех уровнях независимой переменной.
    * Если мы построим регрессию, где зависимой переменной будет квадрат остатков модели *Y* ~ *X*, а независимой переменной будет предиктор *X*, и в этой модели окажется высокий и значимый <a href="https://www.codecogs.com/eqnedit.php?latex=R^{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?R^{2}" title="R^{2}" /></a>, это означает, что в данных есть гетероскедастичность. Тест Бройша — Пагана (Breusch-Pagan test), тест Уайта (White test).
6. Отсутствие автокорреляции остатков.

**Множественная линейная регрессия**

Позволяет исследовать влияние сразу нескольких независимых переменных на одну зависимую переменную: <a href="https://www.codecogs.com/eqnedit.php?latex=y&space;=&space;b_{0}&space;&plus;&space;b_{1}&space;\cdot&space;x_{1}&space;&plus;&space;...&space;&plus;&space;b_{n}&space;\cdot&space;x_{n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y&space;=&space;b_{0}&space;&plus;&space;b_{1}&space;\cdot&space;x_{1}&space;&plus;&space;...&space;&plus;&space;b_{n}&space;\cdot&space;x_{n}" title="y = b_{0} + b_{1} \cdot x_{1} + ... + b_{n} \cdot x_{n}" /></a>.

К условиям применимости добавляются проверка на мультиколлинеарность (сильная связь или идентичность некоторых независимых переменных) и нормальное распределение переменных (желательно).

**_Исправленный_** <a href="https://www.codecogs.com/eqnedit.php?latex=R^{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?R^{2}" title="R^{2}" /></a> – скорректированный коэффициент детерменации. Рассчитывается при включении в модель дополнительных независимых переменных.

**Смешнная регрессионная модель**

**_Эффект_** – влияние независимой переменной, с помощью которой мы предсказываем зависимую переменную.

**_Фиксированный эффект_** _(main effect)_ – влияние независимой переменной, представляющее основной интерес для исследователя.

**_Случайный эффект_** _(random mixed effect)_ – влияние независимой переменной, не представляющее основной интерес для исследователя.

## Задача классификации

**Логистическая регрессия** – исследование взаимосвязи между номинативной зависимой переменной, имеющей всего 2 градации, и различными независимыми переменными.

**Кластерный анализ** – решает задачу кластеризации, то есть для каждго наблюдения находит те наблюдения, которые очень похожи на него, и те, которые от него отличаются. При этом мы снижаем размерность данных.

## Анализ номинативных данных
**Проверка гипотезы о распределении номинативной переменной**  
<a href="https://www.codecogs.com/eqnedit.php?latex=H_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_{0}" title="H_{0}" /></a> – ожидаемое распределение, <a href="https://www.codecogs.com/eqnedit.php?latex=H_{1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_{1}" title="H_{1}" /></a> – распределение отлично от ожидаемого.  
Наблюдаемые частоты _O (observed)_, ожидаемые частоты _E (expected)_.  
Все наблюдения независимы.

    
 



