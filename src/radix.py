"""Radix sort implementaiton."""


def radix(input_list):
    """Radix sort function."""
    if isinstance(input_list, list):
        buckets = {x: [] for x in range(10)}
        num_sorts = len(str(max(input_list)))
        input_list = [str(num) for num in input_list]
        for idx, num in enumerate(input_list):
            if len(num) < num_sorts:
                input_list[idx] = '0' * (num_sorts - len(num)) + num
        for i in range(num_sorts)[::-1]:
            temp = []
            for number in input_list:
                buckets[int(number[i])].append(number)
            for j in buckets:
                while len(buckets[j]) > 0:
                    temp.append(buckets[j].pop(0))
            input_list = temp
        return [int(result_num) for result_num in input_list]
    else:
        raise TypeError('Lists are only accepted as input.')
