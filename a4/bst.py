# Course: CS261 - Data Structures
# Student Name: Kelley Sharp
# Assignment: Binary Search Tree Implementation - Assignment 4
# Description: Implement a BST class with 16 methods


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE in order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does in-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if cur is None:
            return
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # store value of current node
        values.append(str(cur.value))
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Adds the given value to the tree
        """
        def add_node(cur_root, value):
            """
            Recursive helper method that adds a node to an existing tree
            maintaining the BST property
            """
            if cur_root.value <= value:
                # add the new node at the next available space to the right
                if cur_root.right is None:
                    cur_root.right = TreeNode(value)
                    return
                # if no space is available, recurse to search the next sub tree
                add_node(cur_root.right, value)
            else:
                # add the new node at the next available space to the left
                if cur_root.left is None:
                    cur_root.left = TreeNode(value)
                    return

                add_node(cur_root.left, value)
        # if there are no nodes in the tree, create a root node with the given value
        if self.root is None:
            self.root = TreeNode(value)
            return
        # otherwise start searching for the next available space
        add_node(self.root, value)

    def find(self, node, value):
        """
        Recursive helper method that does a binary search for a node
        with the given value
        """
        if node is None:
            return None
        elif node.value == value:
            return node
        elif value > node.value:
            return self.find(node.right, value)
        else:
            return self.find(node.left, value)

    def find_parent(self, node, child_node):
        """
        Recursive helper method that does a binary search for a node
        with a child that has the given value
        """
        if self.root is child_node:
            # node has no parent
            return None

        if node.left is child_node or node.right is child_node:
            return node
        elif child_node.value > node.value:
            return self.find_parent(node.right, child_node)
        else:
            return self.find_parent(node.left, child_node)

    def contains(self, value: object) -> bool:
        """
        Returns True if the value is in the BinaryTree or False if it is not
        """
        # if there are no nodes in the tree, return False
        if self.root is None:
            return False

        # otherwise search for the node with the given value
        node = self.find(self.root, value)
        if node:
            return True

        return False

    def get_first(self) -> object:
        """
        Returns the value stored at the root node
        """
        # if the tree is empty return None
        if self.root is None:
            return None
        else:
            return self.root.value

    def remove_first(self) -> bool:
        """
        Removes the root node
        """
        if not self.root:
            return False
        return self.remove(self.root.value)

    def remove(self, value) -> bool:
        """
        Removes the first instance of the object with the given value and
        returns True or returns False if no object is removed
        """

        def find_smallest_leaf(node):
            """
            A helper method for remove to find the smallest valued node
            (to be used in the right subtree)
            """
            cur = node
            while cur.left:
                cur = cur.left
            return cur

        def remove_child(parent, child):
            """
            A helper method for remove where a parent node removes
            either the left or right child
            """
            if parent.left is child:
                parent.left = None
            else:
                parent.right = None

        def replace_child(parent, child, new_child):
            """
            A helper method for remove where a parent node replaces
            either the left or right child with a new_child
            """
            if parent.left is child:
                parent.left = new_child
            else:
                parent.right = new_child

        # find the node to remove first
        node = self.find(self.root, value)
        if not node:
            return False

        # find its parent node if it exists
        parent = self.find_parent(self.root, node)

        # if node is a leaf we can just update parent's pointers
        if not node.left and not node.right:
            if parent:
                remove_child(parent, node)
                return True
            else:
                self.root = None
        # if node has two children find the next biggest value from right and replace current node
        elif node.left and node.right:
            next_biggest_node = find_smallest_leaf(node.right)
            if next_biggest_node.value == node.right.value:
                # replace the node to be deleted with its right child
                node.value = node.right.value
                node.right = node.right.right
            else:
                # call remove on the next biggest node
                self.remove(next_biggest_node.value)
                # then replace the current node with the next biggest node's value
                node.value = next_biggest_node.value
        # in the else case, the node has one child so it can be replaced with it
        else:
            child_node = node.left or node.right

            if parent:
                replace_child(parent, node, child_node)
            else:
                # the child becomes the new root
                if node is self.root:
                    self.root = child_node
                else:
                    node.value = child_node.value
                    remove_child(node, child_node)


        return True

    def pre_order_traversal(self) -> Queue:
        """
        Returns a queue object of values of nodes visited after a pre order traversal
        """
        result = Queue()

        def traverse(node):
            """
            Recursive helper method that traverses the tree and visits nodes in pre-order
            """
            if node:
                result.enqueue(node.value)
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)
        return result

    def in_order_traversal(self) -> Queue:
        """
        Returns a queue object of values of nodes visited after an in order traversal
        """
        result = Queue()

        def traverse(node):
            """
            Recursive helper method that traverses the tree and visits nodes in order
            """
            if node:
                traverse(node.left)
                result.enqueue(node.value)
                traverse(node.right)

        traverse(self.root)
        return result

    def post_order_traversal(self) -> Queue:
        """
        Returns a queue object of values of nodes visited after a post-order traversal
        """
        result = Queue()

        def traverse(node):
            """
            Recursive helper method that traverses the tree and visits nodes in post-order
            """
            if node:
                traverse(node.left)
                traverse(node.right)
                result.enqueue(node.value)

        traverse(self.root)
        return result

    def by_level_traversal(self) -> Queue:
        """
        Returns a queue object of values of nodes visited after a breadth first traversal
        """

        def level(node):
            """
            Helper method to traverse tree by level
            """
            # keep a queue that resulting values will be stored in
            result = Queue()

            # keep a queue to use for traversing
            q = Queue()

            # enqueue root node to initialize with a value
            if node is self.root:
                q.enqueue(node)

            # breadth-first style iteration per-level
            while not q.is_empty():
                curr = q.dequeue()
                result.enqueue(curr)
                if curr.left is not None:
                    q.enqueue(curr.left)
                if curr.right is not None:
                    q.enqueue(curr.right)

            return result

        return level(self.root)

    def is_full(self) -> bool:
        """
        Determine if the BST is full (every node has zero or two children)
        """
        def traverse_and_check(node):
            """
            Recurse and check the children of each node
            """
            # base case - null node can count as full
            if not node:
                return True
            # if exactly left or right is missing, that's a violation
            if (node.left and not node.right) or (node.right and not node.left):
                return False
            return traverse_and_check(node.left) and traverse_and_check(node.right)

        return traverse_and_check(self.root)

    def is_complete(self) -> bool:
        """
        Determine if the BST is complete (every level except last is filled and nodes are left as possible).
        """
        # an empty tree is complete
        if not self.root:
            return True

        # queue up for breadth-first traversal
        q = Queue()
        q.enqueue(self.root)

        # keep track of whether the previous node was None
        #  since a complete tree will never have two 'None' nodes in a row
        prev_is_none = False

        while not q.is_empty():
            cur = q.dequeue()
            if not cur:
                prev_is_none = True
            else:
                if prev_is_none:
                    return False
                q.enqueue(cur.left)
                q.enqueue(cur.right)

        return True

    def is_perfect(self) -> bool:
        """
        Determine if the BST is perfect (all leaves at the same level and all nodes have exactly two children)
        """

        def find_leaf_depth():
            """
            Find the depth of an arbitrary leaf
            """
            depth = 0
            cur = self.root
            while (cur):
                # count every time we iterate down a level
                depth += 1
                cur = cur.left
            return depth

        def traverse(node, leaf_depth, depth):
            """
            Recurse and check the depth of every leaf
            """
            # base case - an empty tree is perfect
            if not node:
                return True
            # if both are missing we have a leaf
            if not node.left and not node.right:
                if depth + 1 == leaf_depth:
                    return True
                else:
                    # if the depth is wrong we violate the depth rule
                    return False
            # if exactly left or right is missing, we violate the two children rule
            if not node.left or not node.right:
                return False

            return traverse(node.left, leaf_depth, depth + 1) and traverse(node.right, leaf_depth, depth + 1)

        leaf_depth = find_leaf_depth()

        return traverse(self.root, leaf_depth, 0)

    def size(self) -> int:
        """
        Returns the total number of nodes in the tree
        """
        # traverse the tree and store the resulting queue
        result = self.pre_order_traversal()
        size = 0
        i = 0
        # remove each value, adding to the size count each time
        while not result.is_empty():
            size += 1
            result.dequeue()
            i += 1

        return size

    def height(self) -> int:
        """
        Returns the height of the binary tree, returns -1 if the tree is empty
        """
        def traverse_and_count(node, height=0):
            # base case, empty subtree subtracts 1
            if not node:
                return -1
            # the height is defined as the larger of the left subtree or right subtree
            #  at each recursive level we add 1
            return 1 + max(traverse_and_count(node.left), traverse_and_count(node.right))

        return traverse_and_count(self.root)

    def count_leaves(self) -> int:
        """
        Returns the number of nodes in the tree that have no children
        """
        def traverse_and_count(node):
            """
            Recursive helper method that traverses the tree and counts nodes without children
            """
            # base case 1 - no node doesn't count
            if not node:
                return 0
            # base case 2 - node without children counts as 1 leaf
            elif node.left is None and node.right is None:
                return 1
            else:
                # combine the left and the right subtree's leaves
                return traverse_and_count(node.left) + traverse_and_count(node.right)

        return traverse_and_count(self.root)

    def count_unique(self) -> int:
        """
        Returns the number of nodes with unique values in the tree
        """

        # if we do an in-order traversal we get a sorted queue
        queue = self.in_order_traversal()
        if queue.is_empty():
            return 0

        # iterate through the queue, counting the total elements
        #  and the duplicates then subtract the duplicates to get uniques
        prev = queue.dequeue()
        element_count = 1
        duplicate_count = 0

        while not queue.is_empty():
            cur = queue.dequeue()
            element_count += 1
            if cur == prev:
                duplicate_count += 1
            prev = cur

        return element_count - duplicate_count

# BASIC TESTING - PDF EXAMPLES


if __name__ == '__main__':
    # """ add() example #1 """
    # print("\nPDF - method add() example 1")
    # print("----------------------------")
    # tree = BST()
    # print(tree)
    # tree.add(10)
    # tree.add(15)
    # tree.add(5)
    # print(tree)
    # tree.add(15)
    # tree.add(15)
    # print(tree)
    # tree.add(5)
    # print(tree)

    # """ add() example 2 """
    # print("\nPDF - method add() example 2")
    # print("----------------------------")
    # tree = BST()
    # tree.add(10)
    # tree.add(10)
    # print(tree)
    # tree.add(-1)
    # print(tree)
    # tree.add(5)
    # print(tree)
    # tree.add(-1)
    # print(tree)

    # """ contains() example 1 """
    # print("\nPDF - method contains() example 1")
    # print("---------------------------------")
    # tree = BST([10, 5, 15])
    # print(tree.contains(15))
    # print(tree.contains(-10))
    # print(tree.contains(15))

    # """ contains() example 2 """
    # print("\nPDF - method contains() example 2")
    # print("---------------------------------")
    # tree = BST()
    # print(tree.contains(0))

    # """ get_first() example 1 """
    # print("\nPDF - method get_first() example 1")
    # print("----------------------------------")
    # tree = BST()
    # print(tree.get_first())
    # tree.add(10)
    # tree.add(15)
    # tree.add(5)
    # print(tree.get_first())
    # print(tree)

    # """ remove() example 1 """
    # print("\nPDF - method remove() example 1")
    # print("-------------------------------")
    # tree = BST([10, 5, 15])
    # print(tree.remove(7))
    # print(tree.remove(15))
    # print(tree.remove(15))

    # """ remove() example 2 """
    # print("\nPDF - method remove() example 2")
    # print("-------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree.remove(20))
    # print(tree)

    # """ remove() example 3 """
    # print("\nPDF - method remove() example 3")
    # print("-------------------------------")
    # tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    # print(tree.remove(20))
    # print(tree)
    # # comment out the following lines
    # # if you have not yet implemented traversal methods
    # # print(tree.pre_order_traversal())
    # # print(tree.in_order_traversal())
    # # print(tree.post_order_traversal())
    # # print(tree.by_level_traversal())

    # """ remove_first() example 1 """
    # print("\nPDF - method remove_first() example 1")
    # print("-------------------------------------")
    # tree = BST([10, 15, 5])
    # print(tree.remove_first())
    # print(tree)

    # """ remove_first() example 2 """
    # print("\nPDF - method remove_first() example 2")
    # print("-------------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7])
    # print(tree.remove_first())
    # print(tree)

    # """ remove_first() example 3 """
    # print("\nPDF - method remove_first() example 3")
    # print("-------------------------------------")
    # tree = BST([10, 10, -1, 5, -1])
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)

    # """ Traversal methods example 1 """
    # print("\nPDF - traversal methods example 1")
    # print("---------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())

    # """ Traversal methods example 2 """
    # print("\nPDF - traversal methods example 2")
    # print("---------------------------------")
    # tree = BST([10, 10, -1, 5, -1])
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())

    # """ Comprehensive example 1 """
    # print("\nComprehensive example 1")
    # print("-----------------------")
    # tree = BST()
    # header = 'Value   Size  Height   Leaves   Unique   '
    # header += 'Complete?  Full?    Perfect?'
    # print(header)
    # print('-' * len(header))
    # print(f'  N/A {tree.size():6} {tree.height():7} ',
    #       f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #       f'{str(tree.is_complete()):10}',
    #       f'{str(tree.is_full()):7} ',
    #       f'{str(tree.is_perfect())}')

    # for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
    #     tree.add(value)
    #     print(f'{value:5} {tree.size():6} {tree.height():7} ',
    #           f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #           f'{str(tree.is_complete()):10}',
    #           f'{str(tree.is_full()):7} ',
    #           f'{str(tree.is_perfect())}')
    # print()
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())

    # """ Comprehensive example 2 """
    # print("\nComprehensive example 2")
    # print("-----------------------")
    # tree = BST()
    # header = 'Value   Size  Height   Leaves   Unique   '
    # header += 'Complete?  Full?    Perfect?'
    # print(header)
    # print('-' * len(header))
    # print(f'N/A   {tree.size():6} {tree.height():7} ',
    #       f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #       f'{str(tree.is_complete()):10}',
    #       f'{str(tree.is_full()):7} ',
    #       f'{str(tree.is_perfect())}')

    # for value in 'DATA STRUCTURES':
    #     tree.add(value)
    #     print(f'{value:5} {tree.size():6} {tree.height():7} ',
    #           f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #           f'{str(tree.is_complete()):10}',
    #           f'{str(tree.is_full()):7} ',
    #           f'{str(tree.is_perfect())}')
    # print('', tree.pre_order_traversal(), tree.in_order_traversal(),
    #       tree.post_order_traversal(), tree.by_level_traversal(),
    #       sep='\n')
