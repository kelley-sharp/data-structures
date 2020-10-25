# Course: CS261 - Data Structures
# Student Name: Kelley Sharp
# Assignment: A2 - Part 4
# Description: Implement a Queue ADT class
# Last revised: 10/24/2020

from dynamic_array import DynamicArray


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new queue based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self):
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.length()

    def enqueue(self, value: object) -> None:
        """
        Adds a new value to the end of the queue
        """

        # use dynamic array method append to add the value
        self.da.append(value)

    def dequeue(self) -> object:
        """
        Removes the value from beginning of the queue and returns it
        """

        # if the queue is empty, raise error
        if self.is_empty():
            raise QueueException

        # save value of first queue element
        first_val = self.da.get_at_index(0)

        # use dynamic array method remove_at_index to remove the value
        self.da.remove_at_index(0)

        return first_val


# BASIC TESTING
if __name__ == "__main__":

    # print("\n# enqueue example 1")
    # q = Queue()
    # print(q)
    # for value in [1, 2, 3, 4, 5]:
    #     q.enqueue(value)
    # print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))
