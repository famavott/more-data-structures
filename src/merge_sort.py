"""Implementation of merge sort."""


def merge_sort(input_list):
    """Merge sort function to split lists and recurrisvely call on left/right side."""
    if isinstance(input_list, list):
        if len(input_list) <= 1:
            return input_list
        split = len(input_list) // 2
        left = merge_sort(input_list[:split])
        right = merge_sort(input_list[split:])
        return build_list(left, right)
    else:
        raise TypeError('Function only accepts list.')


def build_list(left, right):
    """Build final result list with left and right sides."""
    left_idx = 0
    right_idx = 0
    final = []
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            final.append(left[left_idx])
            left_idx += 1
        else:
            final.append(right[right_idx])
            right_idx += 1
    final += left[left_idx:]
    final += right[right_idx:]
    return final


if __name__ == '__main__':
    import timeit as ti
    sort_1 = [1, 2, 4, 9, 10, 11]
    sort_2 = [17, 9, 7, 4, 1, 0]

    time_1 = ti.timeit("merge_sort(sort_1)",
                       setup="from __main__ import sort_1, merge_sort")
    time_2 = ti.timeit("merge_sort(sort_2)",
                       setup="from __main__ import sort_2, merge_sort")

print("""
    Input: [1, 2, 4, 9, 10, 11]
    Good case: {}

    Input: [17, 9, 7, 4, 1, 0]
    Bad case: {}""".format(time_1, time_2))
