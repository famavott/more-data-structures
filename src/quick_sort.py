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
