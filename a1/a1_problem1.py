# Course: CS261 - Data Structures
# Student Name: Kelley Sharp
# Assignment: Min Max
# Description: function that returns
# the min and max of an array of integers


from a1_include import StaticArray


def min_max(arr: StaticArray) -> ():
    """Receives a StaticArray and Returns a tuple containing two integers,
    the minimum value in the given array and the maximum value in the given array
    """

    # initialize variables
    min_num = arr[0]
    max_num = arr[0]

    # find the minimum value in the array by comparing each value to the current minimum
    for i in range(arr.size()):
        if arr[i] < min_num:
            min_num = arr[i]
        if arr[i] > max_num:
            max_num = arr[i]

    return (min_num, max_num)


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    arr = StaticArray(5)
    for i, value in enumerate([8, 7, 6, -5, 4]):
        arr[i] = value
    print(min_max(arr))

    # example 2
    arr = StaticArray(1)
    arr[0] = 100
    print(min_max(arr))

    # example 3
    arr = StaticArray(3)
    for i, value in enumerate([3, 3, 3]):
        arr[i] = value
    print(min_max(arr))
