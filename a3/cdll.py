# Course: CS261 - Data Structures
# Student Name: Kelley Sharp
# Assignment: Deque and Bag ADT interfaces
# Description: Implement Deque and Bag ADT interfaces with a circular doubly linked list


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list

        This can also be used as troubleshooting method. This method works
        by independently measuring length during forward and backward
        traverse of the list and return the length if results agree or error
        code of -1 or -2 if thr measurements are different.

        Return values:
        >= 0 - length of the list
        -1 - list likely has an infinite loop (forward or backward)
        -2 - list has some other kind of problem

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # length of the list measured traversing forward
        count_forward = 0
        cur = self.sentinel.next
        while cur != self.sentinel and count_forward < 101_000:
            count_forward += 1
            cur = cur.next

        # length of the list measured traversing backwards
        count_backward = 0
        cur = self.sentinel.prev
        while cur != self.sentinel and count_backward < 101_000:
            count_backward += 1
            cur = cur.prev

        # if any of the result is > 100,000 -> list has a loop
        if count_forward > 100_000 or count_backward > 100_000:
            return -1

        # if counters have different values -> there is some other problem
        return count_forward if count_forward == count_backward else -2

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sentinel.next is self.sentinel

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        Adds a new node at the beginning of the list (after the first sentinel)
        """
        new_node = DLNode(value)

        if self.sentinel.next is self.sentinel:
            self.sentinel.next = new_node
            self.sentinel.prev = new_node
            new_node.next = self.sentinel
            new_node.prev = self.sentinel
        else:
            existing_front = self.sentinel.next
            existing_front.prev = new_node
            new_node.next = existing_front
            new_node.prev = self.sentinel
            self.sentinel.next = new_node

    def add_back(self, value: object) -> None:
        """
        Adds a new node at the end of the list (before the sentinel)
        """
        new_node = DLNode(value)

        # if list is empty
        if self.sentinel.next is self.sentinel:
            self.sentinel.next = new_node
            self.sentinel.prev = new_node
            new_node.next = self.sentinel
            new_node.prev = self.sentinel
        else:
            # traverse the list to find last node and add the new node
            cur = self.sentinel.next
            while cur is not self.sentinel:
                if cur.next is self.sentinel:
                    cur.next = new_node
                    new_node.next = self.sentinel
                    new_node.prev = cur
                    self.sentinel.prev = new_node
                    break
                cur = cur.next

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adds a new value at the specified index position in the linked list. Index 0
        refers to the beginning of the list (right after the front sentinel)
        """
        # if the index is invalid, throw an error
        if index < 0 or index > self.length():
            raise CDLLException

        if index == 0:
            self.add_front(value)
            return

        if index == self.length():
            self.add_back(value)
            return

        new_node = DLNode(value)

        # traverse the list until the index is reached and change the pointers
        cur = self.sentinel.next
        i = 0
        while cur.next:
            if i == index:
                new_node.next = cur
                new_node.prev = cur.prev
                cur.prev.next = new_node
                cur.prev = new_node
                break
            cur = cur.next
            i += 1

    def remove_front(self) -> None:
        """
        Removes the node at the front of the list
        """
        # if the list is empty, throw an error
        if self.sentinel.next is self.sentinel:
            raise CDLLException
        else:
            # update the one after the front's prev pointer
            self.sentinel.next.next.prev = self.sentinel
            # update the front to skip over the current front
            self.sentinel.next = self.sentinel.next.next

    def remove_back(self) -> None:
        """
        Removes the last node from the list
        """
        # if the list is empty, throw an error
        if self.sentinel.next is self.sentinel:
            raise CDLLException
        else:
            cur = self.sentinel.next
            while cur.next is not self.sentinel:
                # stop at second to last
                if cur.next.next is self.sentinel:
                    # skip over last
                    cur.next = self.sentinel
                    self.sentinel.prev = cur
                    break
                cur = cur.next

    def remove_at_index(self, index: int) -> None:
        """
        Removes the node from the list given its index. Index 0 refers to the beginning of the list
        """
        # if the index is invalid, throw error
        if index < 0 or index > self.length() - 1:
            raise CDLLException

        if index == 0:
            self.remove_front()
            return

        if index == self.length() - 1:
            self.remove_back()
            return

        # traverse the list until the index is reached and change the pointers
        cur = self.sentinel.next
        i = 0
        while i < self.length():
            if i == index:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                break
            cur = cur.next
            i += 1

    def get_front(self) -> object:
        """
        Returns value from the first node in the list without removing it
        """
        # if the list is empty, throw and error
        if self.sentinel.next is self.sentinel:
            raise CDLLException
        else:
            return self.sentinel.next.value

    def get_back(self) -> object:
        """
        Returns value from the last node in the list without removing it
        """
        # if the list is empty, throw and error
        if self.sentinel.next is self.sentinel:
            raise CDLLException
        else:
            cur = self.sentinel.next
            while cur.next:
                if cur.next is self.sentinel:
                    return cur.value
                cur = cur.next

    def remove(self, value: object) -> bool:
        """
        Removes the first node in the list that matches the provided “value” object.
        Method returns True if some node was actually removed from the list.
        Otherwise it returns False
        """
        cur = self.sentinel.next
        i = 0
        while i < self.length():
            if cur.value == value:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return True
            cur = cur.next
            i += 1

        return False

    def count(self, value: object) -> int:
        """
        Counts the number of elements in the list that match the provided “value” object
        """
        count = 0

        if self.sentinel.prev.value == value:
            count += 1

        cur = self.sentinel.next
        while cur.next is not self.sentinel:
            if cur.value == value:
                count += 1
            cur = cur.next

        return count

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        Swaps two nodes given their indices by changing node pointers.
        """
        # if indices are invalid, throw error
        if index1 < 0 or index1 > self.length() - 1 or index2 < 0 or index2 > self.length() - 1:
            raise CDLLException

        cur = self.sentinel.next
        node1 = None
        node2 = None
        i = 0
        while cur is not self.sentinel:
            if i == index1:
                node1 = cur
            if i == index2:
                node2 = cur
            if node1 and node2:
                # update node2 siblings
                node2.prev.next = node1
                node2.next.prev = node1
                # update node1 siblings
                node1.prev.next = node2
                node1.next.prev = node2
                # swap
                new_node2_next = node1.next
                new_node2_prev = node1.prev
                node1.next = node2.next
                node1.prev = node2.prev
                node2.next = new_node2_next
                node2.prev = new_node2_prev
                
                break
                
            cur = cur.next
            i += 1

    def reverse(self) -> None:
        """
        Reverses the order of the nodes in the list. The reversal must be done “in
        place” without creating any copies of existing nodes or an entire existing list.
        Done by changing node pointers.
        """
        cur = self.sentinel.next
        while cur is not self.sentinel:
            next_node = cur.next
            prev_node = cur.prev

            cur.next = prev_node
            cur.prev = next_node
      
            cur = next_node

    def sort(self) -> None:
        """
        Sorts the content of the list in non-descending order. The sorting is done
        “in place” without creating any copies of existing nodes or an entire existing list.
        """ 
  
        # Traverse through all nodes and change pointers to swap orders
        # cur = self.sentinel.next
        # i = 0
        # j = 0
        # while i < self.length() - 1:
        #     while j < self.length() - i - 1:


    def rotate(self, steps: int) -> None:
        """
        Rotates the linked list by shifting positions of its elements right or left steps
        number of times. If steps is a positive integer, elements should be rotated right. Otherwise,
        rotation is to the left. All work is done “in place” without creating any copies of
        existing nodes or an entire existing list.
        """
        pass

    def remove_duplicates(self) -> None:
        """
        deletes all nodes that have duplicate values from a sorted linked list, leaving
        only nodes with distinct values. Done “in place” without creating any copies
        of existing nodes or an entire existing list.
        """
        cur = self.sentinel.next.next
        prev = self.sentinel.next
        i = 1
        while cur is not self.sentinel:
            if cur.value == prev.value:
                self.remove_at_index(i)
            else:
                i += 1
            prev = cur
            cur = cur.next

    def odd_even(self) -> None:
        """
        Regroups list nodes by first grouping all ODD nodes together followed by all
        EVEN nodes (references are to node numbers in the list, starting from 1, not their values).
        All work must be done “in place” without creating any copies of existing nodes or an entire
        existing list.
        """
        pass


if __name__ == '__main__':
    pass

    # print('\n# add_front example 1')
    # lst = CircularList()
    # print(lst)
    # lst.add_front('A')
    # lst.add_front('B')
    # lst.add_front('C')
    # print(lst)
    #
    # print('\n# add_back example 1')
    # lst = CircularList()
    # print(lst)
    # lst.add_back('C')
    # lst.add_back('B')
    # lst.add_back('A')
    # print(lst)
    
    # print('\n# insert_at_index example 1')
    # lst = CircularList()
    # test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    # for index, value in test_cases:
    #     print('Insert of', value, 'at', index, ': ', end='')
    #     try:
    #         lst.insert_at_index(index, value)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    #
    # print('\n# remove_front example 1')
    # lst = CircularList([1, 2])
    # print(lst)
    # for i in range(3):
    #     try:
    #         lst.remove_front()
    #         print('Successful removal', lst)
    #     except Exception as e:
    #         print(type(e))
    #
    # print('\n# remove_back example 1')
    # lst = CircularList()
    # try:
    #     lst.remove_back()
    # except Exception as e:
    #     print(type(e))
    # lst.add_front('Z')
    # lst.remove_back()
    # print(lst)
    # lst.add_front('Y')
    # lst.add_back('Z')
    # lst.add_front('X')
    # print(lst)
    # lst.remove_back()
    # print(lst)
    #
    # print('\n# remove_at_index example 1')
    # lst = CircularList([1, 2, 3, 4, 5, 6])
    # print(lst)
    # for index in [0, 0, 0, 2, 2, -2]:
    #     print('Removed at index:', index, ': ', end='')
    #     try:
    #         lst.remove_at_index(index)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    # print(lst)
    
    # print('\n# get_front example 1')
    # lst = CircularList(['A', 'B'])
    # print(lst.get_front())
    # print(lst.get_front())
    # lst.remove_front()
    # print(lst.get_front())
    # lst.remove_back()
    # try:
    #     print(lst.get_front())
    # except Exception as e:
    #     print(type(e))
    #
    # print('\n# get_back example 1')
    # lst = CircularList([1, 2, 3])
    # lst.add_back(4)
    # print(lst.get_back())
    # lst.remove_back()
    # print(lst)
    # print(lst.get_back())
    #
    # print('\n# remove example 1')
    # lst = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(lst)
    # for value in [7, 3, 3, 3, 3]:
    #     print(lst.remove(value), lst.length(), lst)
    #
    # print('\n# count example 1')
    # lst = CircularList([1, 2, 3, 1, 2, 2])
    # print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))
    #
    # print('\n# swap_pairs example 1')
    # lst = CircularList([0, 1, 2, 3, 4, 5, 6])
    # test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5),
    #               (4, 2), (3, 3), (1, 2), (2, 1))
    
    # for i, j in test_cases:
    #     print('Swap nodes ', i, j, ' ', end='')
    #     try:
    #         lst.swap_pairs(i, j)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    #
    print('\n# reverse example 1')
    test_cases = (
        [1, 2, 3, 3, 4, 5],
        [1, 2, 3, 4, 5],
        ['A', 'B', 'C', 'D']
    )
    for case in test_cases:
        lst = CircularList(case)
        lst.reverse()
        print(lst)
    
    print('\n# reverse example 2')
    lst = CircularList()
    print(lst)
    lst.reverse()
    print(lst)
    lst.add_back(2)
    lst.add_back(3)
    lst.add_front(1)
    lst.reverse()
    print(lst)
    
    print('\n# reverse example 3')
    
    
    class Student:
        def __init__(self, name, age):
            self.name, self.age = name, age
    
        def __eq__(self, other):
            return self.age == other.age
    
        def __str__(self):
            return str(self.name) + ' ' + str(self.age)
    
    
    s1, s2 = Student('John', 20), Student('Andy', 20)
    lst = CircularList([s1, s2])
    print(lst)
    lst.reverse()
    print(lst)
    print(s1 == s2)
    
    print('\n# reverse example 4')
    lst = CircularList([1, 'A'])
    lst.reverse()
    print(lst)
    #
    # print('\n# sort example 1')
    # test_cases = (
    #     [1, 10, 2, 20, 3, 30, 4, 40, 5],
    #     ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
    #     [(1, 1), (20, 1), (1, 20), (2, 20)]
    # )
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print(lst)
    #     lst.sort()
    #     print(lst)
    #
    # print('\n# rotate example 1')
    # source = [_ for _ in range(-20, 20, 7)]
    # for steps in [1, 2, 0, -1, -2, 28, -100]:
    #     lst = CircularList(source)
    #     lst.rotate(steps)
    #     print(lst, steps)
    #
    # print('\n# rotate example 2')
    # lst = CircularList([10, 20, 30, 40])
    # for j in range(-1, 2, 2):
    #     for _ in range(3):
    #         lst.rotate(j)
    #         print(lst)
    #
    # print('\n# rotate example 3')
    # lst = CircularList()
    # lst.rotate(10)
    # print(lst)
    #
    # print('\n# remove_duplicates example 1')
    # test_cases = (
    #     [1, 2, 3, 4, 5], [1, 1, 1, 1, 1],
    #     [], [1], [1, 1], [1, 1, 1, 2, 2, 2],
    #     [0, 1, 1, 2, 3, 3, 4, 5, 5, 6],
    #     list("abccd"),
    #     list("005BCDDEEFI")
    # )
    
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print('INPUT :', lst)
    #     lst.remove_duplicates()
    #     print('OUTPUT:', lst)
    
    # print('\n# odd_even example 1')
    # test_cases = (
    #     [1, 2, 3, 4, 5], list('ABCDE'),
    #     [], [100], [100, 200], [100, 200, 300],
    #     [100, 200, 300, 400],
    #     [10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E']
    # )
    
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print('INPUT :', lst)
    #     lst.odd_even()
    #     print('OUTPUT:', lst)
