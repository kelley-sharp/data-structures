def remove_occurrences(self, value):
    """
    Removes occurrences of all elements with the given value
    """
    cur = self.sentinel.next
    while cur is not self.sentinel:
        next_node = cur.next
        if cur.value == value:
            cur.prev.next = cur.next
            next_node.prev = cur.prev

        cur = next_node

