def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_list[k] = left[i]
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            my_list[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            my_list[k] = right[j]
            k += 1
            j += 1


my_list = [5, 4, 3, 2, 1]
merge_sort(my_list)
print(my_list)