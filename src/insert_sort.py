"""Implementation of insert sort."""


def insert_sort(input_list):
    """Insert sort function."""
    if isinstance(input_list, list):
        for i in range(len(input_list) - 1):
            for j in range(i + 1, 0, -1):
                if input_list[j] < input_list[j - 1]:
                    temp = input_list[j]
                    input_list[j] = input_list[j - 1]
                    input_list[j - 1] = temp
        return input_list
    else:
        raise TypeError('Function only accepts lists')


if __name__ == '__main__':  # pragma no cover
    import timeit as ti
    sort_1 = [1, 2, 4, 9, 10, 11]
    sort_2 = [17, 9, 7, 4, 1, 0]

    time_1 = ti.timeit("insert_sort(sort_1)",
                       setup="from __main__ import sort_1, insert_sort")
    time_2 = ti.timeit("insert_sort(sort_2)",
                       setup="from __main__ import sort_2, insert_sort")
    print("""
        Input: [1, 2, 4, 9, 10, 11]
        Good case: {}

        Input: [17, 9, 7, 4, 1, 0]
        Bad case: {}""".format(time_1, time_2))
