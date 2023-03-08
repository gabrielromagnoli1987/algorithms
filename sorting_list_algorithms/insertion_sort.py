def insertion_sort(sample_list):
    # https://youtu.be/GzyOEmu_Jv8
    """ runtime complexity O(n^2) """
    for i in range(1, len(sample_list)):
        value = sample_list[i]
        j = i
        while j > 0 and sample_list[j - 1] > value:
            sample_list[j] = sample_list[j - 1]
            j = j - 1
        sample_list[j] = value
    return sample_list
