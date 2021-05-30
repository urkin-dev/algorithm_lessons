class Solution(object):
    def sortArray(self, nums):
        arr = nums

        for i in range(len(arr)):
            arr[i] = int(arr[i])

        arr = self.heapSort(arr)

        return arr

    # Основная функция для сортировки массива заданного размера
    def heapSort(self, arr):
        n = len(arr)

        # Построение max-heap.
        for i in range(n, -1, -1):
            self.heapify(arr, n, i)

        # Один за другим извлекаем элементы
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # свап
            self.heapify(arr, i, 0)

        return arr

    # Процедура для преобразования в двоичную кучу поддерева с корневым узлом i, что является индексом в arr[]. n - размер кучи
    def heapify(self, arr, n, i):
        largest = i  # Initialize largest as root
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
            arr[i], arr[largest] = arr[largest], arr[i]  # свап

            # Применяем heapify к корню.
            self.heapify(arr, n, largest)
