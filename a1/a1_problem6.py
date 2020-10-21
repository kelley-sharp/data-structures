# Course: CS261 - Data Structures
# Student Name: Kelley Sharp
# Assignment: Is Sorted?
# Description: Function that receives a StaticArray and returns
# an integer that describes whether the array is sorted, 1 for
# being in strictly ascending order, 2 for being sorted in
# strictly descending order, and 0 if the array is not sorted


from a1_include import StaticArray


def is_sorted(arr: StaticArray) -> int:
    """
    Receives a StaticArray and returns:
    1 if the array is sorted in strictly ascending order
    2 if the array is sorted in strictly descending order
    0 if the array is not strictly sorted
    """

    # if only one element in the StaticArray, it is considered
    # sorted in strictly ascending order so return 1
    if arr.size() == 1:
        return 1

    # initialize a variable to hold the integer representing the sort order
    sort_int = None

    # loop through StaticArray keeping track of previous and current values
    # store current sort order in new_sort_int variable and compare that
    # with sort_int on each iteration, updating sort_int each time or returning 0
    # if they are different
    prev = arr[0]
    for i in range(1, arr.size()):
        new_sort_int = 0
        current = arr[i]
        if current == prev:
            new_sort_int = 0
        elif current > prev:
            new_sort_int = 1
        elif current < prev:
            new_sort_int = 2

        if sort_int is None:
            sort_int = new_sort_int
        elif sort_int != new_sort_int:
            return 0

        prev = arr[i]

    return sort_int


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '1'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)
