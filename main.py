from sorting_list_algorithms.bubble_sort import bubble_sort
from sorting_list_algorithms.insertion_sort import insertion_sort
from sorting_list_algorithms.merge_sort import merge_sort
from sorting_list_algorithms.quick_sort import quick_sort
from sorting_list_algorithms.selection_sort import selection_sort

if __name__ == '__main__':
    sample_list = [3, 1, 5, 7, 2, 4, 6, 9, 8]
    print(f"Original list: \n{sample_list}")
    print(f"After bubble sort: \n{bubble_sort(sample_list)}\n")

    sample_list = [3, 1, 5, 7, 2, 4, 6, 9, 8]
    print(f"Original list: \n{sample_list}")
    print(f"After selection sort: \n{selection_sort(sample_list)}\n")

    sample_list = [3, 1, 5, 7, 2, 4, 6, 9, 8]
    print(f"Original list: \n{sample_list}")
    print(f"After insertion sort: \n{insertion_sort(sample_list)}\n")

    sample_list = [3, 1, 5, 7, 2, 4, 6, 9, 8]
    print(f"Original list: \n{sample_list}")
    print(f"After merge sort: \n{merge_sort(sample_list)}\n")

    sample_list = [3, 1, 5, 7, 2, 4, 6, 9, 8]
    print(f"Original list: \n{sample_list}")
    print(f"After quick sort: \n{quick_sort(sample_list)}\n")
