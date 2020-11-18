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

    def find(self, cur_node, value):
        """
        Recursive helper method that does a binary search for a node
        with the given value
        """
        if cur_node is None:
            return None
        elif cur_node.value == value:
            return cur_node
        elif value > cur_node.value:
            return self.find(cur_node.right, value)
        else:
            return self.find(cur_node.left, value)

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
        # if the tree is empty
        if self.root is None:
            return False

        # if root has no children, empty the tree
        elif self.root.left is None and self.root.right is None:
            self.root = None
            return True

        # if there is no right node, replace with the left node
        elif self.root.right is None:
            self.root = self.root.left
            return True

        else:
            # if there is a right node:

            # if the right node has no left node, replace the root with the right node
            # and assign it the root's left node as it's left node
            if self.root.right.left is None:
                temp = self.root.left
                self.root = self.root.right
                self.root.left = temp
                return True

            # find the root node's in order successor and the successor's parent
            cur_node = self.root.right
            ps = None
            s = None

            while cur_node.left:
                if cur_node.left.left is None:
                    ps = cur_node
                    s = cur_node.left
                    break
                else:
                    cur_node = cur_node.left

            # replace the root node with it's in order successor
            temp = self.root.left
            ps.left = s.right
            self.root = s
            self.root.right = ps
            self.root.left = temp

            return True

    def remove(self, value) -> bool:
        """
        Removes the first instance of the object with the given value and
        returns True or returns False if no object is removed
        """

        def find_parent(cur_node, child_node_value):
            """
            Recursive helper function to find the parent of given child node
            """
            if cur_node.right.value == value or cur_node.left.value == value:
                return cur_node
            else:
                return find_parent(cur_node.right, child_node_value)
                return find_parent(cur_node.left, child_node_value)

        # if the tree is empty
        if self.root is None:
            return False

        # if the node to be removed is the root node call remove_first
        if self.root.value == value:
            self.remove_first()
            return True

        # identify the node to be removed
        node = self.find(self.root, value)

        # if the value was not in the tree
        if node is None:
            return False

        # identify the parent of the node
        pn = find_parent(self.root, value)

        # if node does not have a right or left node
        if node.right is None and node.left is None:
            # if node is a right child of the parent
            if pn.right is node:
                pn.right = None
                return
            # if node is a left child of the parent
            if pn.left is node:
                pn.left = None
                return

        # if node has only a left child, and no right child
        if node.left and node.right is None:
            # if node is a left child of parent node
            if pn.left is node:
                pn.left = node.left
            # if node is a right child of parent node
            if pn.right is node:
                pn.right = node.left

        # if node has a right node:
        # identify the in order successor
        cur_node = node.right
        ps = None
        s = None

        while cur_node.left:
            if cur_node.left.left is None:
                ps = cur_node
                s = cur_node.left
                break
            else:
                cur_node = cur_node.left

        # if node has only a right child, and no left child
        if node.right and node.left is None:
            # if node is a left child of parent node
            if pn.left is node:
                pn.left = node.right
            # if node is a right child of parent node
            if pn.right is node:
                pn.right = node.right

        # if node has both a left child and right child
        if node.right and node.left:
            node.value = s.value
            # if the in order successor has a right child
            if s.right:
                ps.left = s.right
            else:
                ps.left = None

        return True

    def pre_order_traversal(self) -> Queue:
        """
        Returns a queue object of values of nodes visited after a pre order traversal
        """
        result = Queue()

        def pre(node):
            """
            Recursive helper method that traverses the tree and visits nodes in pre-order
            """
            if node:
                result.enqueue(node.value)
                pre(node.left)
                pre(node.right)

        pre(self.root)
        return result

    def in_order_traversal(self) -> Queue:
        """
        Returns a queue object of values of nodes visited after an in order traversal
        """
        result = Queue()

        def in_order(node):
            """
            Recursive helper method that traverses the tree and visits nodes in order
            """
            if node:
                in_order(node.left)
                result.enqueue(node.value)
                in_order(node.right)

        in_order(self.root)
        return result

    def post_order_traversal(self) -> Queue:
        """
        Returns a queue object of values of nodes visited after a post-order traversal
        """
        result = Queue()

        def post(node):
            """
            Recursive helper method that traverses the tree and visits nodes in post-order
            """
            if node:
                post(node.left)
                post(node.right)
                result.enqueue(node.value)

        post(self.root)
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

            # keep a queue to use while traversing
            q = Queue()

            # enqueue root node to initialize with a value
            if node is self.root:
                q.enqueue(node)

            while (not q.is_empty()):
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
        TODO: Write this implementation
        """
        return True

    def is_complete(self) -> bool:
        """
        TODO: Write this implementation
        """
        return True

    def is_perfect(self) -> bool:
        """
        TODO: Write this implementation
        """
        return True

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
        # if tree is empty
        if self.root is None:
            return -1

        # if tree only consists of root node
        if self.root.right is None and self.root.left is None:
            return 0

        def max_height(node):
            """
            Helper function that determines which subtree of the node has the longest height
            """


        return max_height(self.root)

    def count_leaves(self) -> int:
        """
        Returns the number of nodes in the tree that have no children
        """
        # if the tree is empty
        if self.root.left is None and self.root.right is None:
            return 0

        def in_order_leaf_count(node):
            """
            Recursive helper method that traverses the tree and counts nodes without children
            """
            count = 0
            if node:
                in_order_leaf_count(node.left)
                if node.left is None and node.right is None:
                    count += 1
                in_order_leaf_count(node.right)
            return count

        return in_order_leaf_count(self.root)


    def count_unique(self) -> int:
        """
        use trav
        """
        return 0



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
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())

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

    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

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

