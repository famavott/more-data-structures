"""Implementation of merge sort."""


def merge_sort(input_list):
    """Merge sort function to split lists and recurrisvely call on left/right side, then add to results list."""
    if isinstance(input_list, list):
        center = len(input_list) // 2
        left = input_list[:center]
        right = input_list[center:]
        if len(left) > 1:
            left = merge_sort(left)
        if len(right) > 1:
            right = merge_sort(right)
        result = []
        while left and right:
            if left[-1] >= right[-1]:
                result.append(left.pop())
            else:
                result.append(right.pop())
        return (left or right) + result[::-1]
    else:
        raise TypeError('Function only accepts list.')


if __name__ == '__main__':  # pragma no cover
    import timeit as ti
    sort_1 = [1, 2, 4, 9, 10, 11]
    sort_2 = [17, 9, 7, 4, 1, 0]
    sort_3 = [x for x in range(21, 1, -1)]

    time_1 = ti.timeit("merge_sort(sort_1[:])",
                       setup="from __main__ import sort_1, merge_sort")
    time_2 = ti.timeit("merge_sort(sort_2[:])",
                       setup="from __main__ import sort_2, merge_sort")
    time_3 = ti.timeit("merge_sort(sort_3[:])",
                       setup="from __main__ import sort_3, merge_sort")

print("""
    Input: [1, 2, 4, 9, 10, 11]
    Good case: {}

    Input: [17, 9, 7, 4, 1, 0]
    Bad case: {}

    Input: [x for x in range(101, 1, -1)]
    Time: {}
    """.format(time_1, time_2, time_3))
