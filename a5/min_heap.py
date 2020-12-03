# Course: CS261 - Data Structures
# Assignment: 5
# Student: Kelley Sharp
# Description: Implement the MinHeap class, complete with 4 methods


# Import pre-written DynamicArray and LinkedList classes
from a5_include import DynamicArray
import math


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Adds a new object to the MinHeap maintaining the heap property
        """
        # Put new node at the end of the array
        self.heap.append(node)
        # bubble it up from the end of the heap
        self.heapify_up()

    def get_min(self) -> object:
        """
        Returns an object with a minimum key without removing it from the heap
        """
        if self.heap.length() == 0:
            raise MinHeapException
        return self.heap[0]

    def remove_min(self) -> object:
        """
        Removes the object with the minimum key from the heap and returns it
        """
        if self.is_empty():
            raise MinHeapException

        result = self.heap[0]

        # edge case, just remove single element if only 1 exists
        if self.heap.length() == 1:
            self.heap.pop()
        else:
            # replace the top element with the bottom and then re-heapify
            self.heap[0] = self.heap.pop()
            self.heapify_down()
        return result

    def get_parent_index(self, child_index):
        """
        Helper method to compute the index of the parent
        """
        return math.floor((child_index - 1) / 2)

    def get_left_child_index(self, parent_index):
        """
        Helper method to compute the index of the left child
        """
        return (2 * parent_index) + 1

    def get_right_child_index(self, parent_index):
        """
        Helper method to compute the index of the right child
        """
        return (2 * parent_index) + 2

    def swap(self, index_1, index_2):
        """
        Helper method to swap two values at provided indices
        """
        self.heap[index_1], self.heap[index_2] = self.heap[index_2], self.heap[index_1]

    def heapify_up(self):
        """
        Take the element at the end of the array and find its correct position
        """
        current_idx = self.heap.length() - 1
        parent_idx = self.get_parent_index(current_idx)

        # swap while there is a parent and the parent is larger than the current element
        while parent_idx >= 0 and self.heap[parent_idx] > self.heap[current_idx]:
            self.swap(current_idx, parent_idx)
            current_idx = self.get_parent_index(current_idx)
            parent_idx = self.get_parent_index(current_idx)

    def heapify_down(self, start_idx=0):
        """
        Take the element at the beginning of the array or at the given position
        and find its final position in the heap
        """
        current_index = start_idx
        next_index = None
        # get (possible) indices of both children
        left_child_index = self.get_left_child_index(current_index)
        right_child_index = self.get_right_child_index(current_index)

        # while there is a left child
        while left_child_index < self.heap.length():
            left_child = self.heap[left_child_index]

            # if there is also a right child, compare the left and right child to determine where to swap down
            if right_child_index < self.heap.length():
                right_child = self.heap[right_child_index]

                if left_child <= right_child:
                    next_index = left_child_index
                else:
                    next_index = right_child_index
            # otherwise prepare to swap with the left
            else:
                next_index = left_child_index

            # break early if the heap ordering is correct
            if self.heap[current_index] < self.heap[next_index]:
                return

            # swap and iterate down
            self.swap(current_index, next_index)
            current_index = next_index
            left_child_index = self.get_left_child_index(current_index)
            right_child_index = self.get_right_child_index(current_index)

    def build_heap(self, da: DynamicArray) -> None:
        """
        Takes a dynamic array with objects in any order and builds a proper MinHeap from them
        """
        self.heap = DynamicArray()
        for i in range(da.length()):
            self.heap.append(da[i])
        for i in range(self.heap.length() - 1, -1, -1):
            self.heapify_down(i)


# BASIC TESTING
if __name__ == '__main__':
    pass
    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
