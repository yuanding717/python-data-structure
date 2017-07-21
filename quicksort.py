def quicksort(array):
    _quicksort(array, 0, len(array) - 1)


def _quicksort(array, left, right):
    if left < right:
        pi = partition(array, left, right)
        print pi, array
        _quicksort(array, left, pi - 1)
        _quicksort(array, pi + 1, right)


def partition(array, left, right):
    i = left
    pivot = array[right]
    for j in range(left, right):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[right] = array[right], array[i]
    return i


test = [1, 10, 2, 11, 9]
quicksort(test)
print test