# Course: CS261 - Data Structures
# Student Name: Kelley Sharp
# Assignment: Rotate
# Description: Function that receives two parameters - a StaticArray
# and an integer value (called steps). It returns a new StaticArray
# where all elements from the original array exist, but are shifted
# right or left steps number of times.


from a1_include import StaticArray


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Receives a StaticArray and an integer value. Returns
    a new StaticArray with elements from the original
    array moved the specified number of times in
    either a right (positive integer) or left
    (negative integer) direction
    """
    # initialize new StaticArray
    rotated_arr = StaticArray(arr.size())

    # loop through original StaticArray
    # mod by the size to get the new index to ensure that
    # the new index will always be in bounds
    for i in range(arr.size()):
        rotated_arr[(i + steps) % arr.size()] = arr[i]

    return rotated_arr


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100]:
        print(rotate(arr, steps), steps)
    print(arr)
