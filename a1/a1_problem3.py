# Course: CS261 - Data Structures
# Student Name: Kelley Sharp
# Assignment: Reverse
# Description: Function that receives a StaticArray and reverses the order
# of the elements in the array 'in place'


from a1_include import StaticArray


def reverse(arr: StaticArray) -> None:
    """
    Receives a StaticArray and reverses it in place
    """

    # loop through each index and swap its value with the element opposite it from the middle
    i = 0
    while i < arr.size() // 2:
        complement_idx = (arr.size() - 1) - i
        temp = arr[i]
        arr[i] = arr[complement_idx]
        arr[complement_idx] = temp
        i += 1


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)
