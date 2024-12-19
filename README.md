# HT_Perfomance_Lab
Тестовые задания для компании HT Perfomance Lab.

Внимание! Ввод данных во всех задачах выполняется непосредственно с помощью cmd.

## Task1:

Круговой массив - массив из элементов, в котором по достижению конца массива
следующим элементом будет снова первый. Массив задается числом n, то есть
представляет собой числа от 1 до n.

Пример:

>n = 5;
>
>m = 4

Решение:

Круговой массив: 12345.

При длине обхода 4 получаем интервалы: 1234, 4512, 2345, 5123, 3451.

Полученный путь: 14253.

Для запуска укажем путь и аргументы <n> <m> через пробел:
>> ## python circle_array.py n m

## Task2:

Напишите программу, которая рассчитывает положение точки относительно
окружности.

Координаты центра окружности и его радиус считываются из файла 1.

Пример:

> 1 1
> 
> 5
> 
Координаты точек считываются из файла 2.

Пример:

> 0 0
> 
> 1 6
> 
> 6 6

● файл с координатами и радиусом окружности - 1 аргумент;

● файл с координатами точек - 2 аргумент;

● координаты - рациональные числа в диапазоне от 10^-38 до 10^38;

● количество точек от 1 до 100;

● вывод каждого положения точки заканчивается символом новой строки;

● соответствия ответов:

○ 0 - точка лежит на окружности

○ 1 - точка внутри

○ 2 - точка снаружи.

В репозитории представлены 2 текстовых файла: file_1 и file_2 они и будут являться аргументами для запуска нашей программы!

file_1 содержит в себе координаты центра окружности и радиус 

file_2 содержит точки соответственно

Для запуска укажем путь и аргументы <file_1> <file_2> через пробел:
>> ## python point_position.py file_1.txt file_2.txt

## Task3:
На вход в качестве аргументов программы поступают три пути к файлу (в приложении
к заданию находятся примеры этих файлов):

● values.json содержит результаты прохождения тестов с уникальными id

● tests.json содержит структуру для построения отчета на основе прошедших
тестов (вложенность может быть большей, чем в примере)

● report.json - сюда записывается результат.

Напишите программу, которая формирует файл report.json с заполненными полями
value для структуры tests.json на основании values.json.

Структура report.json такая же, как у tests.json, только заполнены поля “value”.

task3 соответственно содержит все указанные выше файлы и сохраняет указанную логику каждого из них.

Для запуска укажем путь и аргументы values.json tests.json report.json через пробел:

>> ## python collect_values.py <values.json> <tests.json> <report.json>

## Task4:
Дан массив целых чисел nums.

Напишите программу, выводящую минимальное количество ходов, требуемых для
приведения всех элементов к одному числу.

За один ход можно уменьшить или увеличить число массива на 1.

На вход подаётся файл с содержимым:

>1
>
>10
>
>2
>
>9
>
Вывод в консоль: 16

Для запуска укажем путь и аргументы <nums.txt>  через пробел:
>> ## python same_numbers.py nums.txt


