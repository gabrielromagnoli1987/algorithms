def merge_sort(sample_list):
    # https://youtu.be/ZUJK2mgn8I8
    # https://www.educative.io/answers/merge-sort-in-python
    """ runtime complexity O(n*log(n)) """
    if len(sample_list) > 1:
        mid = len(sample_list) // 2
        left = sample_list[:mid]
        right = sample_list[mid:]
        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)
        # Two iterators for traversing the two halves
        i = 0
        j = 0
        # Iterator for the main list
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # The value from the left half has been used
                sample_list[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                sample_list[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            sample_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            sample_list[k] = right[j]
            j += 1
            k += 1
    return sample_list
