# Изображение проекции полиэдра

42. Все рёбра делятся на три класса: полностью видимые, видимые частично и полностью невидимые. Назовём грань «гранью с полностью видимыми рёбрами», если все образующие её рёбра полностью видимы. Если все образующие грань рёбра полностью невидимы, то грань будем называть «гранью с полностью невидимыми рёбрами». Все остальные грани будем называть «гранями с частично видимыми рёбрами». Модифицируйте эталонный проект таким образом, чтобы определялась и печаталась следующая характеристика полиэдра: сумма площадей проекций «граней с полностью видимыми рёбрами», образующих с горизонтальной плоскостью угол не более 
 центр которых находится строго вне куба единичного объёма с центром в начале координат и рёбрами, параллельными координатным осям.

![Шахматный король](images/king.png)

## Проверка соблюдения соглашений о стиле программного кода

~~~{.sh}
find . -name '*.py' -exec pycodestyle {} \;
~~~

## Проверка покрытия тестами кода программы

~~~{.sh}
python -B -m coverage run -m unittest discover tests && coverage report -m ; rm -f .coverage
~~~
