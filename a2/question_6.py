def dynArrayAddAt(self, index: int, value: object) -> None:
    """
    Adds an element at a particular index in the array
    """

    # if given index is invalid, raise error
    if index < 0 or index > self.size:
        raise Exception

    # if current elements plus one max out capacity, double the capacity to make room
    if self.size + 1 == self.capacity:

        # create a StaticArray with double the capacity
        double_cap_arr = StaticArray(self.capacity * 2)

        # reference any existing values to this new StaticArray
        for i in range(self.size):
            double_cap_arr[i] = self.data[i]

        # replace data with this new StaticArray
        self.data = double_cap_arr

        # reset the capacity
        self.capacity = self.capacity * 2

    # Move every value after given index further right by one
    for i in range(self.size - 1, index - 1, - 1):
        self.data[i + 1] = self.data[i]

    # insert value at given index
    self.data[index] = value

    self.size += 1
