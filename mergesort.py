def mergesort(input_array):
    _mergesort(input_array, 0, len(input_array) - 1)


def _mergesort(input_array, left, right):
    if left < right:
        mid = left + (right - left) / 2
        _mergesort(input_array, left, mid)
        _mergesort(input_array, mid + 1, right)
        merge(input_array, left, mid, right)
        print input_array


def merge(input_array, left, mid, right):
    left_len = mid - left + 1
    right_len = right - mid
    left_array = input_array[left : mid + 1]
    right_array = input_array[mid + 1: right + 1]
    i, j = 0, 0
    k = left
    while i < left_len and j < right_len:
        if left_array[i] <= right_array[j]:
            input_array[k] = left_array[i]
            i += 1
        else:
            input_array[k] = right_array[j]
            j += 1
        k += 1
    while i < left_len:
        input_array[k] = left_array[i]
        i += 1
        k += 1
    while j < right_len:
        input_array[k] = right_array[j]
        j += 1
        k += 1


input_array = [21, 4, 1, 3, 9, 20, 25]
mergesort(input_array)
print ("\nSorted array is")
print input_array