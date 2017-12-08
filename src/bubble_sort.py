"""Bubble sort implementation."""


def bubble_sort(input_list):
    """Bubble sort function."""
    if isinstance(input_list, list):
        swaps = 1
        while swaps:
            swaps = 0
            for i in range(len(input_list) - 1):
                if input_list[i] > input_list[i + 1]:
                    temp = input_list[i]
                    input_list[i] = input_list[i + 1]
                    input_list[i + 1] = temp
                    swaps += 1
            if swaps == 0:
                return input_list
    else:
        raise TypeError('Function only accepts lists')


if __name__ == '__main__':  # pragma no cover
    import timeit as ti
    sort_1 = [1, 2, 4, 9, 10, 11]
    sort_2 = bubble_sort([17, 9, 7, 4, 1, 0])

    time_1 = ti.timeit("bubble_sort(sort_1[:])",
                       setup="from __main__ import sort_1, bubble_sort")
    time_2 = ti.timeit("bubble_sort(sort_2[:])",
                       setup="from __main__ import sort_2, bubble_sort")
    print("""
        Input: [1, 2, 4, 9, 10, 11]
        Good case: {}

        Input: [17, 9, 7, 4, 1, 0]
        Bad case: {}""".format(time_1, time_2))
