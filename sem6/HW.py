# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве.

# Используемые парадигмы: структурная и процедурная


def binary_search(arr, n):
    first = 0
    last = len(arr) - 1

    while first <= last:
        mid = (last + first)//2
        n1 = arr[mid]
        if n1 == n:
            return mid
        if n1 > n:
            last = mid - 1
        else :
            first = mid + 1
    return None

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = 2
print(binary_search(array, num))