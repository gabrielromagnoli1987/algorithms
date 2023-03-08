def selection_sort(sample_list):
    # https://youtu.be/0MdfSjSnPe0
    """ runtime complexity O(n^2) """
    for i in range(len(sample_list) - 1):
        min_value = sample_list[i]
        min_index = i
        for j in range(i + 1, len(sample_list)):
            if sample_list[j] < min_value:
                min_value = sample_list[j]
                min_index = j
        sample_list[i], sample_list[min_index] = sample_list[min_index], sample_list[i]
    return sample_list
