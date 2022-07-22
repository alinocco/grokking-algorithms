from random import randrange


def merge_sort(array):

    if len(array) > 1:
        middle = len(array) // 2

        left_array = array[:middle]
        right_array = array[middle:]

        merge_sort(left_array)
        merge_sort(right_array)

        # Merge
        i = j = k = 0
        while i < len(left_array) and j < len(right_array):
            if(left_array[i] <= right_array[j]):
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1

            k += 1

        # Check if some elements were left
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1


array = [randrange(10000) for i in range(10)]
print(array)
merge_sort(array)
print(array)
