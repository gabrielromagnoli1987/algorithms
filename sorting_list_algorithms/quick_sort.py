def quick_sort(sample_list):
    # https://youtu.be/kLYqVGTKE20
    # https://youtu.be/DYmTpUfcyT8
    """ runtime complexity O(n*log(n)) """
    if len(sample_list) == 1:
        return sample_list
    if len(sample_list) == 0:
        return []

    left = []
    right = []
    pivot = sample_list[0]

    for i in sample_list[1:]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)
