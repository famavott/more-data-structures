"""Implementation of quick sort."""


def quick_sort(input_list):
    """Quick sort function that accepts input_list."""
    if len(input_list) <= 1:
        return input_list
    lesser, pivot, greater = partition(input_list)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)


def partition(input_list):
    """Divide input list into two halves with a pivot point."""
    pivot = input_list[0]
    seq = input_list[1:]
    lesser = [x for x in seq if x <= pivot]
    greater = [x for x in seq if x > pivot]
    return lesser, pivot, greater
