# Course: CS261 - Data Structures
# Student Name: Kelley Sharp
# Assignment: Remove Duplicates
# Description: Function that takes a sorted StaticArray
# and returns a new StaticArray with duplicate values removed


from a1_include import StaticArray


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Receives a sorted StaticArray and returns a new StaticArray
    with duplicates removed
    """

    # initialize a variable to store a count of duplicates
    dup_count = 0

    # loop through the original StaticArray and add to dup_count when a dupe is encountered
    for i in range(1, arr.size()):
        prev = arr[i - 1]
        current = arr[i]
        if current == prev:
            dup_count += 1

    # create a new StaticArray the size of the original StaticArray subtracting the number of duplicates
    no_dupe_sa = StaticArray(arr.size() - dup_count)

    # loop through the original StaticArray again,
    # this time setting values of non-dupes as values in the no_dupe_sa:

    # initialize an index keeper to use when setting values
    insert_index = 0

    # initialize a variable to store the previous value
    prev = None

    for i in range(arr.size()):
        if i > 0:
            prev = arr[i - 1]
        current = arr[i]
        if current != prev:
            no_dupe_sa.set(insert_index, current)
            insert_index += 1

    return no_dupe_sa


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)
