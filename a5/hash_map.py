# Course: CS261 - Data Structures
# Assignment: 5
# Student: Kelley Sharp
# Description: Implement the HashMap class with 9 methods


# Import pre-written DynamicArray and LinkedList classes
from a5_include import DynamicArray, LinkedList, SLNode


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        Clears the content of the hash map, without changing the capacity
        """
        # Loop through the length of buckets and re-initialize each bucket's linked list
        # with a head that has a value of None
        for i in range(self.buckets.length()):
            self.buckets[i].head = None

        self.size = 0

    def get(self, key: str) -> object:
        """
        Returns the value associated with the given key
        """
        # Get the index we should look for the key in
        index = self.hash_function(key) % self.capacity

        # Loop through the linked list at that index to search for the key
        ll = self.buckets[index]
        cur = ll.head
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next

        # If there is no such key in the hash table
        return None

    def put(self, key: str, value: object) -> None:
        """
        Upserts the key / value pair in the hash map
        """
        # Find the index to insert the new node, provided by the hash function
        index = self.hash_function(key) % self.capacity

        # If a linked list already exists at that index, search for the key
        if self.buckets[index]:
            # Loop to see if the key is in the linked list, if so, update its value
            cur = self.buckets[index].head
            while cur:
                if cur.key == key:
                    cur.value = value
                    return
                cur = cur.next

            # If the key does not already exist in the linked list, add the key / value pair as a new node
            self.buckets[index].insert(key, value)
            self.size += 1
        else:
            # Otherwise update the linked list at the index with this node as the head
            new_node = SLNode(key, value)
            ll = self.buckets[index]
            ll.head = new_node
            self.size += 1

    def remove(self, key: str) -> None:
        """
        Removes the given key and its associated value from the hash map
        """
        # Get the index to look for key
        index = self.hash_function(key) % self.capacity

        # Get the linked list at index and remove if found
        ll = self.buckets[index]
        if ll.remove(key):
            ll.remove(key)
            self.size -= 1

    def contains_key(self, key: str) -> bool:
        """
        Returns true if the given key is in the hash map
        """
        # If hash map is empty
        if self.buckets.length() == 0:
            return False

        else:
            # Find index to look for key in and loop through linked list at that index
            index = self.hash_function(key) % self.capacity
            cur = self.buckets[index].head
            while cur:
                if cur.key == key:
                    return True
                cur = cur.next

            # If the key was not found
            return False

    def empty_buckets(self) -> int:
        """
        Returns the number of empty buckets in the hash table
        """
        # loop over the buckets and keep count of empty buckets
        empty = 0
        for bucket in self.buckets:
            if bucket.head is None:
                empty += 1

        return empty

    def table_load(self) -> float:
        """
        Returns the current hash table load factor
        """
        # find total number of elements stored in the table
        total_elements = 0
        for ll in self.buckets:
            if ll.length():
                total_elements += ll.length()

        # find the number of buckets (capacity)
        buckets = self.capacity

        # return load factor
        return total_elements / buckets

    def resize_table(self, new_capacity: int) -> None:
        """
        Changes the capacity of the hash table unless new_capacity is less than 1
        """
        if new_capacity < 1:
            return
        else:
            # Create a new hash map with new capacity
            new_hm = HashMap(new_capacity, self.hash_function)

            # Get the keys from the current hash map
            # rehash each and assign to the new index in the new hash map via the put method
            for i in range(self.buckets.length()):
                if self.buckets[i]:
                    cur = self.buckets[i].head
                    while cur:
                        new_hm.put(cur.key, cur.value)
                        cur = cur.next

            # replace the current hash map with the new one
            self.buckets = new_hm.buckets
            self.capacity = new_hm.capacity

    def get_keys(self) -> DynamicArray:
        """
        Returns a DynamicArray that contains all keys stored in the hash map
        """
        keys_arr = DynamicArray()

        # Loop through buckets and add keys to the new array as we find them
        for i in range(self.buckets.length()):
            if self.buckets[i]:
                cur = self.buckets[i].head
                while cur:
                    keys_arr.append(cur.key)
                    cur = cur.next

        return keys_arr


# BASIC TESTING
if __name__ == "__main__":
    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))

    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())
