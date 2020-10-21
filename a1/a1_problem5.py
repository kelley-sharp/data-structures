# Course: CS261 - Data Structures
# Student Name: Kelley Sharp
# Assignment: Range
# Description: Function that receives two integers and returns a
# StaticArray that contains consecutive values starting with the
# first integer and ending with the last


from a1_include import StaticArray


def sa_range(start: int, end: int) -> StaticArray:
    """
    Receives two integers, start and end, and returns a Static Array
    that contains consecutive values beginning at start and ending at
    end (inclusive)
    """

    # determine if start is a greater or lesser value than end
    count = 1
    if start > end:

        # loop to determine the size needed for the StaticArray
        for num in range(end, start):
            count += 1

        # initialize new StaticArray with this size and save in a variable
        range_arr = StaticArray(count)

        # loop to set each index with the value from start to end
        value = start
        i = 0
        while value >= end:
            range_arr.set(i, value)
            value -= 1
            i += 1
    else:
        # loop to determine the size needed for the StaticArray
        for num in range(start, end):
            count += 1

        # initialize new StaticArray with this size and save in a variable
        range_arr = StaticArray(count)

        # loop to set each index with the value from start to end
        value = start
        i = 0
        while value <= end:
            range_arr.set(i, value)
            value += 1
            i += 1
    return range_arr


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    # cases = [(0, -3), (-99, -105)]
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-105, -99), (-99, -105)]
    for start, end in cases:
        print(start, end, sa_range(start, end))
