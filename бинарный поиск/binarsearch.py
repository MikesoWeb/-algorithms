# Бинарный поиск

def binary_search(list, item):
    low = 0                     # начальная граница списка в которой осуществляется поиск
    high = len(list) - 1        # позиция последнего элемента списка

    while low <= high:          # пока диапазон не сузится что они буду равны
        mid = low + high        # находим средний элемент
        guess = list[mid]       # значение середины элемента списка кладем в переменную
        if item == guess:       # если значение середины равно ввдененому значниею
            return mid          # то возвращаем порядковый номер этого элемента
        if guess > item:        # Если оно больше чем введеное
            high = mid - 1      # то значние среднего элемента уменьшаем на 1 и кладем в переменную цикла
        else:
            high = mid + 1      # Если значние меньше
    return none

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3)) # выводит порядковый номер наденного элемента
        

    

def logarifm_2(number):         # функция определяющая логарифм 2 от числа 
    count = 2                   # переменная на которую будем перемножать
    i = 1                       # счетчик для подсчета количества умножений
    while count < number:       # пока 2 число меньше числа веденного пользоваталем
        count = count * 2       # 2 умножаем на саму себя 
        i = i + 1               # в счетчик добавляем 1
        if count == number:     # если умножение на 2 значение равно числу введенному пользователем
            return i            # возвращаем число счетчика
    return None                 # иначе ничего не возвращаем

def logarifm_n(number, n):      # функция определяющая логарифм n от числа number
    count = n                   # переменная на которую будем перемножать
    i = 1                       # счетчик для подсчета количества умножений
    while count < number:       # пока 2 число меньше числа веденного пользоваталем
        count = count * n       # 2 умножаем на саму себя 
        i = i + 1               # в счетчик добавляем 1
        if count == number:     # если умножение на 2 значение равно числу введенному пользователем
            return i            # возвращаем число счетчика
    return None                 # иначе ничего не возвращаем

print(logarifm_2(1024))
print(logarifm_n(1024, 2))
