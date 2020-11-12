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

    def remove_occurrences(self, value):
        cur = self.sentinel.next
        while cur is not self.sentinel:
            next_node = cur.next
            if cur.value == value:
                cur.prev.next = cur.next
                next_node.prev = cur.prev

            cur = next_node


test = CircularList(['a', 'b', 'a', 'c', 'a', 'd', 'a', 'a', 'e'])
print(test)
test.remove_occurrences('a')
print(test)