# Алгоритм быстрой сортировки

def quicksort(array):
    if len(array) < 2:                                          # базовый случай массив 0 и 1 элементоа
        return array                                            # уже являются отсортированным
    else:                                                       #
        pivot = array[0]                                        # рекурсивный случай
        less = [i for i in array[1:] if i <= pivot]             # подмассив всех элементов меньше опорного
        greater = [i for i in array[1:] if i > pivot]           # подмассив всех элементов больше опорного
        return quicksort(less) + [pivot] + quicksort(greater)   #

print(quicksort([10, 5, 2, 3, 55]))
