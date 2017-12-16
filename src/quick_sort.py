"""Implementation of quick sort."""


def quick_sort(input_list):
    """Quick sort function that accepts input_list."""
    if isinstance(input_list, list):
        if len(input_list) <= 1:
            return input_list
        less, equal, greater = [], [], []
        pivot = input_list[0]
        for num in input_list:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        return quick_sort(less) + [pivot] + quick_sort(greater)
    else:
        raise TypeError('Only lists can be passed into function.')

if __name__ == '__main__':  # pragma no cover
    import timeit as ti
    sort_1 = [1, 2, 4, 9, 10, 11]
    sort_2 = [17, 9, 7, 4, 1, 0]

    time_1 = ti.timeit("quick_sort(sort_1[:])",
                       setup="from __main__ import sort_1, quick_sort")
    time_2 = ti.timeit("quick_sort(sort_2[:])",
                       setup="from __main__ import sort_2, quick_sort")
    print("""
        Input: [1, 2, 4, 9, 10, 11]
        Good case: {}

        Input: [17, 9, 7, 4, 1, 0]
        Bad case: {}""".format(time_1, time_2))
