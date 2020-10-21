# Course: CS261 - Data Structures
# Student Name: Kelley Sharp
# Assignment: Fizz Buzz
# Description: Function that takes a StaticArray of integers and returns a new
# StaticArray object with content from the original array, but modified based on certain rules


from a1_include import StaticArray


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Receives an array of integers and returns a new StaticArray object
    with the corresponding strings or integers based on these rules:
    Both a multiple of 3 and 5, add 'fizzbuzz' to the new array,
    only a multiple of 3, add 'fizz' to the new array,
    only a multiple of 5, add 'buzz' to the new array,
    otherwise add an element with the same integer to the new array
    """
    # Create new StaticArray object
    new_SA = StaticArray(arr.size())

    for i in range(arr.size()):

        # If the number is both divisible by 3 and of 5 with no remainder, add 'fizzbuzz' to that index in the new array
        if arr[i] % 3 == 0 and arr[i] % 5 == 0:
            new_SA.set(i, "fizzbuzz")

        # If the number is just divisible by 3, add 'fizz' to that index in the new array
        elif arr[i] % 3 == 0:
            new_SA.set(i, "fizz")

        # If the number is just divisible by 5, add 'buzz' to that index in the new array
        elif arr[i] % 5 == 0:
            new_SA.set(i, "buzz")

        # else add the number to that index in the new array
        else:
            new_SA.set(i, arr[i])

    return new_SA


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)
