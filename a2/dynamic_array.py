# Course: CS261 - Data Structures
# Student Name: Kelley Sharp
# Assignment: A2 - Part 1
# Description: Implement a Dynamic Array class
# Last revised: 10/20/2020


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.first = 0  # do not use / change this value
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    def resize(self, new_capacity: int) -> None:
        """
        Increases or decreases the capacity of the dynamic array to given new_capacity
        If new_capacity is less than the size of current elements, this method will exit
        """

        # if desired capacity is smaller than size of current elements, return
        if new_capacity <= self.size:
            return
        else:
            # create a StaticArray with the desired capacity
            new_cap_arr = StaticArray(new_capacity)

            # reference any existing values to this new StaticArray
            for i in range(self.length()):
                new_cap_arr[i] = self.data[i]

            # replace data with this new StaticArray
            self.data = new_cap_arr

            # reset the capacity
            self.capacity = new_capacity

    def append(self, value: object) -> None:
        """
        Adds element to the end of dynamic array
        """
        # if current elements max out capacity, double the capacity to make room
        if self.size == self.capacity:
            self.resize(2 * self.capacity)

        # assign the value to the next available index in the StaticArray
        self.data[self.size] = value

        # increase size by one
        self.size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts given value as element at index indicated
        """

        # if given index is invalid, raise error
        if index < 0 or index > self.size:
            raise DynamicArrayException

        # if current elements max out capacity, double the capacity to make room
        if self.size == self.capacity:
            self.resize(2 * self.capacity)

        # Move every value after given index further right by one
        for i in range(self.size - 1, index - 1, - 1):
            self.data[i + 1] = self.data[i]

        # insert value at given index
        self.data[index] = value

        self.size += 1

    def get_at_index(self, index: int) -> object:
        """
        Returns value at specific index in the dynamic array
        """

        # if the index is invalid, raise error
        if index < 0 or index > self.size - 1:
            raise DynamicArrayException
        else:
            return self.data[index]

    def remove_at_index(self, index: int) -> None:
        """
        Removes the element from the dynamic array at given index
        """

        # if the index is invalid, raise error
        if index < 0 or index > self.size - 1:
            raise DynamicArrayException

        # if the number of elements is strictly less than 1/4 the array's current capacity
        if self.size < self.capacity / 4 and self.capacity > 10:
            # if reducing the capacity to twice the would make capacity greater than 10
            # reduce the capacity to twice the number of elements
            self.capacity = max(self.size * 2, 10)

        # Move every value after given index further left by one, overwriting the "removed" value
        if (index == self.size - 1):
            self.data[index] = None
        else:
            for i in range(index, self.size - 1):
                self.data[i] = self.data[i + 1]

        self.size -= 1

    def slice(self, start_index: int, quantity: int) -> object:
        """
        Returns a new dynamic array containing the requested number of
        elements from the original array starting with the element located
        at the requested start index
        """

        # if the start index or size is invalid, raise error
        if (start_index < 0) or (start_index > self.size - 1) or (quantity < 0):
            raise DynamicArrayException

        # if there are not enough elements between start index and end of the array
        # to make the slice of requested size, raise error
        if start_index + quantity > self.size:
            raise DynamicArrayException

        # loop from 0 to the quantity, and add elements to a new dynamic array starting
        # at start_index, and increasing 1 each time
        slice_arr = DynamicArray()
        j = start_index
        for i in range(quantity):
            slice_arr.append(self.data[j])
            j += 1

        return slice_arr

    def merge(self, second_da: object) -> None:
        """
        Takes another dynamic array object as a parameter, and appends all
        elements from the second array to the current one, in the same order
        as they are stored in the second array
        """

        # loop through second dynamic array and append each element to the original array
        for i in range(second_da.length()):
            self.append(second_da.get_at_index(i))

    def map(self, map_func) -> object:
        """
        Returns a new dynamic array where the value of each element is derived by
        applying a given map_func to the corresponding value from the original array
        """

        # loop through original dynamic array, pass each value through the map_func provided
        # append each result to a new dynamic array and return the array
        mapped_val_arr = DynamicArray()
        for i in range(self.size):
            mapped_val_arr.append(map_func(self.data[i]))

        return mapped_val_arr

    def filter(self, filter_func) -> object:
        """
        Returns a new dynamic array populated only with those elements from the
        original array for which filter_func returns True
        """

        # loop through original dynamic array, pass each value through the filter_func provided
        # and append each result to a new dynamic array, if the result is True, and return the array
        filtered_val_arr = DynamicArray()
        for i in range(self.size):
            if filter_func(self.data[i]):
                filtered_val_arr.append(self.data[i])

        return filtered_val_arr

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Takes an optional initial value and returns the resulting value after
        applying the reduce_func to all elements of the dynamic array. If the
        dynamic array is empty, returns the initializer or None if no initializer exists
        """

        # keep track of the result, initialize with initializer
        # loop through dynamic array
        starting_index = 0
        if initializer:
            accumulator = initializer
        else:
            accumulator = self.data[0]
            starting_index = 1

        for i in range(starting_index, self.size):
            accumulator = reduce_func(accumulator, self.data[i])

        return accumulator


# BASIC TESTING
if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Can not insert value", value, "at index", index)
    print(da)

    print("\n# get_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50])
    print(da)
    for i in range(4, -1, -1):
        print(da.get_at_index(i))

    print("\n# get_at_index example 2")
    da = DynamicArray([100, 200, 300, 400, 500])
    print(da)
    for i in range(-1, 7):
        try:
            print("Index", i, ": value", da.get_at_index(i))
        except Exception as e:
            print("Index", i, ": exception occurred")

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]          # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 69 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOUCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")
    def double(value):
        return value * 2

    def square(value):
        return value ** 2

    def cube(value):
        return value ** 3

    def plus_one(value):
        return value + 1

    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")
    def filter_a(e):
        return e > 10

    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")
    def is_long_word(word, length):
        return len(word) > length

    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
