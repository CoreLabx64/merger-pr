# Подключение библиотек / Connecting libraries
import os                                                                       # Библиотека работы с файлами / Library for working with files
import time                                                                     # Библиотека работы со временем / Time Library
from PIL import Image                                                           # Библиотека работы с изображениями / Image Library
from random import randint                                                      # Библиотека работы со случайными числами / Library for working with random int
from progress.bar import FillingSquaresBar                                      # Библиотека работы с прогрессом / Progress Library

# Процедура (Цикл) чтения файлов и сбора массива / Procedure (Cycle) of reading files and collect array
def proc_walk(_path, _list):                                                    # Объявление названия процедуры / Declaration of the procedure name
    for root, dirs, files in os.walk(_path):                                    # Присоединение пути / Joining a path
        for file in files:                                                      # Обозначение ячеек / Cell designation
            if(file.endswith(".png")):                                          # Указание типа файлов / Specifying the file type
                _list.append(os.path.join(root,file))                           # Добавление ссылок в массив / Adding links to an array
    return                                                                      # Возврат значений / Return values

# Процедура уникализации изображений / The procedure for image unification
def proc_uniq(_img, _uniq):                                                     # Объявление названия процедуры / Declaration of the procedure name
    uni = Image.open(_img)                                                      # Открытие изображения уникализации / Opening a unicalization image
    uni_n = Image.open(_uniq[0])                                                # Открытие изображения водяного знака / Opening a watermark image
    back = uni.copy()                                                           # Копирование изображения во избежание изменения оригинала / Copying an image to avoid changing the original
    back.paste(uni_n, (5,5), uni_n)                                             # Наложение водяного знака на изображение / Putting watermark on image
    back.save(_img)                                                             # Сохранение результата / Saving the result
    return                                                                      # Возврат значений / Return values

# Объявление глобальных переменных / Declaration of global variables
backgrounds = []                                                                # Массив фонов / Array of Backgrounds
bodies = []                                                                     # Массив тел / Array of Bodies
eyes = []                                                                       # Массив глаз / Array of Eyes
unique = []                                                                     # Массив уникализации / Array of Unique
compiled = []                                                                   # Массив компиляции / Array of Compile
savedname = ''                                                                  # Собирательная переменная / Collective variable
bar_finish, i, x, n, v = 0, 0, 0, 0, 0                                          # Массив переменных / Array of variables

# Обозначение путей к изображениям / Marking paths to images
path_background = 'lmdb\\backgrounds\\'                                         # Путь к изображениям фона / Path to Backgrounds Images
path_bodies     = 'lmdb\\bodies\\'                                              # Путь к изображениям тела / Path to Bodies Images
path_eyes       = 'lmdb\\eyes\\'                                                # Путь к изображениям глаз / Path to Eyes Images
path_unique     = 'lmdb\\unique\\'                                              # Путь к изображениям уникализации / Path to Unique Images
path_compiled   = 'compiled\\'                                                  # Путь для скомпилированных изображений / Path for compiled images

# Вызов процедур / Calling procedures
proc_walk(path_background,backgrounds)                                          # Получение массива фона / Getting a Background array
proc_walk(path_bodies,bodies)                                                   # Получение массива тела / Getting a Bodies array
proc_walk(path_eyes,eyes)                                                       # Получение массива глаз / Getting a Eyes array
proc_walk(path_unique,unique)                                                   # Получение массива уникализации / Getting a Unique array

# Подсчет количества операций для прогресса / Counting the number of operations for progress
bar_finish = len(backgrounds) * len(bodies) * len(eyes)                         # Основной подсчёт операций / Basic counting of operations
print(' Прогресс сбора изображений:')                                           # Форматирование вывода / Output formating       
bar = FillingSquaresBar(max = bar_finish)                                       # Указание данных для прогресса / Specifying data for progress

# Тело (Цикл) сбора окончательного изображения / The body (Cycle) of collecting the final image
if len(backgrounds)==0 or len(bodies)==0 or len(eyes)==0:                       # Проверка условий на пустоту массивов / Checking conditions for empty arrays
    print('Один из массивов пуст, проверьте директории')                        # Вывод ошибки / Error output
else:                                                                           # Выход на выполнение условий / Exit to the fulfillment of conditions
    timer = time.time()                                                         # Начало таймера / Timer started
    for back in backgrounds:                                                    # Обозначение ячеек фона / Cell designation background
        _collect_x = Image.open(back)                                           # Открытие файла фона / Opening a background file
        _collect_x_back = _collect_x.copy()                                     # Копирование изображения во избежание изменения оригинала / Copying an image to avoid changing the original
        for body in bodies:                                                     # Обозначение ячеек тела / Cell designation bodies
            _collect_v = Image.open(body)                                       # Открытие файла тела / Opening a body file
            _collect_v_back = _collect_v.copy()                                 # Копирование изображения во избежание изменения оригинала / Copying an image to avoid changing the original
            _collect_x_back.paste(_collect_v_back, (5,5), _collect_v_back)      # Наложение тела на изображение / Putting body on image
            for eye in eyes:                                                    # Обозначение ячеек глаза / Cell designation eyes
                _collect_n = Image.open(eye)                                    # Открытие файла глаза / Opening the eye file
                _collect_x_back.paste(_collect_n, (160,70), _collect_n)         # Наложение глаз на изображение / Putting eyes on image
                _collect_x_back.save(path_compiled + 'compiled ('               # Сбор пути и запись файла (начало) / Collecting the path and writing the file (start)
                + str(x) + '-'                                                  # /------------ transfer line ------------/
                + str(v) + '-'                                                  # /------------ transfer line ------------/
                + str(n) +').png')                                              # Сбор пути и запись файла (конец) / Collecting the path and writing the file (end)
                n += 1                                                          # Увеличение шага цикла n / Increasing the cycle step n
                bar.next()                                                      # Шаг прогресса / Progress step
            v += 1                                                              # Увеличение шага цикла v / Increasing the cycle step v       
    bar.finish()                                                                # Окончание прогресса / End of progress
    print(' Время затраченное на сбор - ',                                      # Сбор вывода таймера / Collecting timer output
    round(time.time() - timer, 2),                                              # /------------ transfer line ------------/
    ' секунды')                                                                 # Окончание сбора вывода таймера / End of timer output collection

# Тело (Цикл) уникализации изображений / The body (Cycle) of image unicalization
proc_walk(path_compiled,compiled)                                               # Получение массива изображений / Getting a Images array

_count = int(bar_finish * 0.1)                                                  # Вычисление шанса возникновения уникального изображения / Calculating the chance of a unique image

print(' Прогресс уникализации изображений:')                                    # Форматирование вывода / Output formating
ubar = FillingSquaresBar(max = _count)                                          # Указание данных для прогресса / Specifying data for progress
timer = time.time()                                                             # Начало таймера / Timer started
while i < _count:                                                               # Начало цикла уникализации / The beginning of the unicalization cycle
    r = randint(0, bar_finish)                                                  # Создание случайного числа / Creating a random number
    g = r                                                                       # Копия для устранения повторения / Copy to eliminate repetition
    r = randint(0, bar_finish)                                                  # Вторая итерация случайного числа / The second iteration of a random number
    if g == r:                                                                  # Сравнение на повтор / Repeat Comparison
        r = randint(0, bar_finish)                                              # Если повтор то новая генерация / If there is a repeat then a new generation
    img = compiled[r]                                                           # Выбор случайного изображения для уникализации / Choosing a random image for uniqueness
    proc_uniq(img, unique)                                                      # Вызов процедуры уникализации / Calling the unicalization procedure
    i += 1                                                                      # Увеличение шага цикла i / Increasing the cycle step I
    ubar.next()                                                                 # Шаг прогресса / Progress step
ubar.finish()                                                                   # Окончание прогресса / End of progress
print(' Время затраченное на уникализацию - ',                                  # Сбор вывода таймера / Collecting timer output
round(time.time() - timer, 2),                                                  # /------------ transfer line ------------/
' секунды')                                                                     # Окончание сбора вывода таймера / End of timer output collection
    
# ------------------------------------------------- #
# ----------- Space of declaration proc ----------- #
# ------------------------------------------------- #

# Copyright: Создано CoreLabx64 в 2022 году / Created by CoreLabx64 in 2022
