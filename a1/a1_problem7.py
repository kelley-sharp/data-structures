# Course: CS261 - Data Structures
# Student Name: Kelley Sharp
# Assignment: Sort
# Description: Function that sorts a given StaticArray
# in ascending order, in-place


from a1_include import StaticArray


def sa_sort(arr: StaticArray) -> None:
    """
    Receives a StaticArray and uses bubble sort to sort in ascending order
    """

    # loop through the StaticArray and swap values where the second value
    # is smaller than the first until no more swaps can occur
    for i in range(arr.size() - 1):
        for j in range(arr.size() - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        sa_sort(arr)
        print(arr)
