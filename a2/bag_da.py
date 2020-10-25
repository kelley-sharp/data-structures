# Course: CS261 - Data Structures
# Student Name: Kelley Sharp
# Assignment: A2 - Part 2
# Description: Implement a Bag ADT class
# Last revised: 10/24/2020

from dynamic_array import DynamicArray


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()

    def add(self, value: object) -> None:
        """
        Adds a given value to the bag
        """

        # use dynamic array method append to add the given value to the bag
        self.da.append(value)

    def remove(self, value: object) -> bool:
        """
        Removes a given value from the bag if a match was found and returns True
        if no such item that matches the given value is found it returns False
        """

        # loop through bag, if an item matches the given value, remove it and return True
        for i in range(self.size()):
            if self.da.get_at_index(i) == value:
                self.da.remove_at_index(i)
                return True

        return False

    def count(self, value: object) -> int:
        """
        Returns the number of elements found in the bag that match the given value
        """

        # loop through the bag and add matching elements to the count
        count = 0
        for i in range(self.size()):
            if self.da.get_at_index(i) == value:
                count += 1

        return count

    def clear(self) -> None:
        """
        Deletes the contents of the bag
        """

        # re-assign bag to empty dynamic array
        self.da = DynamicArray()

    def equal(self, second_bag: object) -> bool:
        """
        Returns True if the bag is equal to the provided second bag (has the same number
        of elements and contain the same elements without regards to the order of elements)
        Otherwise it returns false
        """

        # check if the bags have the same number of elements
        if self.size() != second_bag.size():
            return False

        if self.size() == 0:
            return True

        # sort both arrays
        def bubbleSort(arr: DynamicArray):
            for i in range(arr.size - 1):
                for j in range(0, arr.size - i - 1):
                    if arr.get_at_index(j) > arr.get_at_index(j + 1):
                        temp = arr.get_at_index(j)
                        arr.data.set(j, arr.get_at_index(j + 1))
                        arr.data.set(j + 1, temp)

        sorted_copy_of_bag_1 = self.da.slice(0, self.size())
        bubbleSort(sorted_copy_of_bag_1)

        sorted_copy_of_bag_2 = second_bag.da.slice(0, self.size())
        bubbleSort(sorted_copy_of_bag_2)

        # loop through and check if each element matches, if not, return False
        for i in range(self.size()):
            if sorted_copy_of_bag_1.get_at_index(i) != sorted_copy_of_bag_2.get_at_index(i):
                return False

        return True


# BASIC TESTING
if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))
