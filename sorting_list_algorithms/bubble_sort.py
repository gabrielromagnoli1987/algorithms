def bubble_sort(sample_list):
    # https://youtu.be/Sr521jBTcto
    """ runtime complexity O(n^2) """
    for i in range(len(sample_list)):
        for j in range(len(sample_list) - i - 1):
            if sample_list[j] > sample_list[j + 1]:
                sample_list[j], sample_list[j + 1] = sample_list[j + 1], sample_list[j]

    return sample_list
