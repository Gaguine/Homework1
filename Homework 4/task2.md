Библиотека pandas

Выполните задания из ноутбука class_5/Pandas.ipynb

Task 1

Вы работаете аналитиком в компании ScienceYou. Ваша задача — проанализировать чистую прибыль.
Доходы (income), расходы (expenses) и годы (years), соответствующие им, предоставлены вам в виде списков.

Например:
```
income = [478, 512, 196]
expenses = [156, 130, 270]
years = [2018, 2019, 2020]
```

Создайте функцию create_companyDF(income, expenses, years), которая  возвращает DataFrame, составленный из входных данных со столбцами Income и Expenses и индексами, соответствующими годам рассматриваемого периода.

Task 2

1. Какова цена объекта недвижимости под индексом 15?
2. Когда был продан объект под индексом 90?


Task 3

1. У скольких объектов недвижимости из таблицы melb_data отсутствуют ванные комнаты?
2. Сколько в таблице melb_data объектов недвижимости, которые были проданы риелтором Nelson и стоимость которых составила больше 3 миллионов?

Task 4

Напишите функцию delete_columns(df, col=[]), которая удаляет столбцы из DataFrame и возвращает новую таблицу. Если одного из указанных столбцов не существует в таблице, то функция должна возвращать None.