"""Implementation of merge sort."""


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


def merge_sort(input_list):
    """Merge sort function to split lists and recurrisvely call on left/right side."""
    if isinstance(input_list, list):
        split = len(input_list) // 2
        left = merge_sort(input_list[:split])
        right = merge_sort(input_list[split:])
        return build_list(left, right)
    else:
        raise TypeError('Function only accepts lists.')
