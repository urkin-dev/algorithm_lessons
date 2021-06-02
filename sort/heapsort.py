import time
from base import getListInput

# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i, что является индексом в arr[]. n - размер кучи
def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2

  # Проверяем существует ли левый дочерний элемент больший, чем корень

    if l < n and arr[i] < arr[l]:
        largest = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # свап

        # Применяем heapify к корню.
        heapify(arr, n, largest)

# Основная функция для сортировки массива заданного размера
def heapSort(arr):
    n = len(arr)

    # Построение max-heap. То есть такую кучу, у которой родительский элемент больше или равен дочерним
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # свап. На первом месте стоит больший элемент, а на последнем меньший
        heapify(arr, i, 0)

def heapSortTime(count):
    list = getListInput(count)
    start = time.time()
    heapSort(list)
    end = time.time()

    return end - start

# Как пример Вход: [4, 10, 3, 5, 1]
# После первого рекурсивного heapify: [10, 5, 3, 4, 1]
# После первого свапа: [1, 5, 3, 4, 10]
# Во второй рекурсивный heapify не пойдет 10, потому что 10 находится на границами и мы сравниваем везде строго до n
# Т.е. в heapify у нас снова построится куча на этот раз с 5 родителем и снова произойдет свап первого и последнего
# последний опять не пойдет в следующий heapify и далее родителем будет 4 и так далее до конца цикла. Получится отсортированный
# по возрастанию массив