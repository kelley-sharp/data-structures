# Course: CS261 - Data Structures
# Student Name:
# Assignment: Part 1 - Deque and Bag ADT 
# Description: Implement Deque and Bag ADT interfaces with a Singly Linked List



class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.head.next == self.tail

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        Adds a new node at the beginning of the list (after the first sentinel)
        """
        if self.head is None:
            new_node = SLNode(value)
            self.head.next = new_node
            new_node.next = self.tail
        else:
            new_node = SLNode(value)
            new_node.next = self.head.next
            self.head.next = new_node

    def add_back(self, value: object) -> None:
        """
        Adds a new node at the end of the list (before the last sentinel)
        """
        new_node = SLNode(value)

        if self.head.next is self.tail:
            self.head.next = new_node
            new_node.next = self.tail
        else:
            # traverse the list to find last node and add the new node
            cur = self.head.next
            while cur.next:
                if cur.next == self.tail:
                    cur.next = new_node
                    new_node.next = self.tail
                cur = cur.next

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adds a new value at the specified index position in the linked list. Index 0
        refers to the beginning of the list (right after the front sentinel)
        """
        # if the index is invalid, throw an error
        if index < 0 or index > self.length():
            raise SLLException

        new_node = SLNode(value)

        if index == 0:
            temp = self.head.next
            self.head.next = new_node
            new_node.next = temp
            return

        # traverse the list until the index is reached and change the pointers
        cur = self.head.next
        i = 0
        while cur.next:
            if i + 1 == index:
                temp = cur.next
                cur.next = new_node
                new_node.next = temp
                break
            cur = cur.next
            i += 1

    def remove_front(self) -> None:
        """
        Removes the node at the front of the list
        """
        # if the list is empty, throw an error
        if self.head.next == self.tail:
            raise SLLException
        else:
            self.head.next = self.head.next.next

    def remove_back(self) -> None:
        """
        Removes the last node from the list
        """
        # if the list is empty, throw an error
        if self.head.next == self.tail:
            raise SLLException
        else:
            # traverse the list to find last node and change the pointers
            cur = self.head.next
            if cur.next == self.tail:
                self.head.next = self.tail
            else:
                while cur.next.next:
                    if cur.next.next == self.tail:
                        cur.next = self.tail
                        break
                    cur = cur.next

    def remove_at_index(self, index: int) -> None:
        """
        Removes the node from the list given its index. Index 0 refers to the beginning of the list
        """
        # if the index is invalid, throw error
        if index < 0 or index > self.length() - 1:
            raise SLLException

        if index == 0:
            self.head.next = self.head.next.next
            return

        # traverse the list until the index is reached and change the pointers
        cur = self.head.next
        i = 0
        while cur.next:
            if i + 1 == index:
                cur.next = cur.next.next
                break
            cur = cur.next
            i += 1

    def get_front(self) -> object:
        """
        Returns value from the first node in the list without removing it
        """
        # if the list is empty, throw and error
        if self.head.next == self.tail:
            raise SLLException
        else:
            return self.head.next.value

    def get_back(self) -> object:
        """
        TODO: Write this implementation
        """
        pass

    def remove(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        pass

    def count(self, value: object) -> int:
        """
        TODO: Write this implementation
        """
        pass

    def slice(self, start_index: int, size: int) -> object:
        """
        TODO: Write this implementation
        """
        pass





if __name__ == '__main__':
    pass

    # print('\n# add_front example 1')
    # list = LinkedList()
    # print(list)
    # list.add_front('A')
    # list.add_front('B')
    # list.add_front('C')
    # print(list)
    #
    #
    # print('\n# add_back example 1')
    # list = LinkedList()
    # print(list)
    # list.add_back('C')
    # list.add_back('B')
    # list.add_back('A')
    # print(list)
    #
    #
    # print('\n# insert_at_index example 1')
    # list = LinkedList()
    # test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    # for index, value in test_cases:
    #     print('Insert of', value, 'at', index, ': ', end='')
    #     try:
    #         list.insert_at_index(index, value)
    #         print(list)
    #     except Exception as e:
    #         print(type(e))
    #
    #
    # print('\n# remove_front example 1')
    # list = LinkedList([1, 2])
    # print(list)
    # for i in range(3):
    #     try:
    #         list.remove_front()
    #         print('Successful removal', list)
    #     except Exception as e:
    #         print(type(e))
    #
    #
    # print('\n# remove_back example 1')
    # list = LinkedList()
    # try:
    #     list.remove_back()
    # except Exception as e:
    #     print(type(e))
    # list.add_front('Z')
    # list.remove_back()
    # print(list)
    # list.add_front('Y')
    # list.add_back('Z')
    # list.add_front('X')
    # print(list)
    # list.remove_back()
    # print(list)
    #
    #
    # print('\n# remove_at_index example 1')
    # list = LinkedList([1, 2, 3, 4, 5, 6])
    # print(list)
    # for index in [0, 0, 0, 2, 2, -2]:
    #     print('Removed at index:', index, ': ', end='')
    #     try:
    #         list.remove_at_index(index)
    #         print(list)
    #     except Exception as e:
    #         print(type(e))
    # print(list)
    #
    #
    print('\n# get_front example 1')
    list = LinkedList(['A', 'B'])
    print(list.get_front())
    print(list.get_front())
    list.remove_front()
    print(list.get_front())
    list.remove_back()
    try:
        print(list.get_front())
    except Exception as e:
        print(type(e))
    #
    #
    # print('\n# get_back example 1')
    # list = LinkedList([1, 2, 3])
    # list.add_back(4)
    # print(list.get_back())
    # list.remove_back()
    # print(list)
    # print(list.get_back())
    #
    #
    # print('\n# remove example 1')
    # list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(list)
    # for value in [7, 3, 3, 3, 3]:
    #     print(list.remove(value), list.length(), list)
    #
    #
    # print('\n# count example 1')
    # list = LinkedList([1, 2, 3, 1, 2, 2])
    # print(list, list.count(1), list.count(2), list.count(3), list.count(4))
    #
    #
    # print('\n# slice example 1')
    # list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # ll_slice = list.slice(1, 3)
    # print(list, ll_slice, sep="\n")
    # ll_slice.remove_at_index(0)
    # print(list, ll_slice, sep="\n")
    #
    #
    # print('\n# slice example 2')
    # list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    # print("SOURCE:", list)
    # slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    # for index, size in slices:
    #     print("Slice", index, "/", size, end="")
    #     try:
    #         print(" --- OK: ", list.slice(index, size))
    #     except:
    #         print(" --- exception occurred.")

