class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Inserts a node with the given data into the binary tree."""
        if self.root is None:
            self.root = Node(data)
            return
        parent = None
        current = self.root
        while True:
            if data < current.data:
                parent = current
                current = current.left
                if current is None:
                    parent.left = Node(data)
                    return
            else:
                parent = current
                current = current.right
                if current is None:
                    parent.right = Node(data)
                    return

    def search(self, data):
        """Searches for a node with the given data in the binary tree."""
        current = self.root
        while current is not None:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def update(self, old_data, new_data):
        """Updates the data of a node with the given old data to the new data."""
        if not self.search(old_data):
            return  # Data not found

        current = self.root
        while True:
            if new_data < current.data:
                if current.left is None:
                    current.left = Node(new_data)
                    return
                current = current.left
            elif new_data > current.data:
                if current.right is None:
                    current.right = Node(new_data)
                    return
                current = current.right
            else:  # Found the node with old_data
                current.data = new_data
                return

    def delete(self, data):
        """Deletes a node with the given data from the binary tree."""
        if self.root is None:
            return  # Tree is empty

        parent = None
        current = self.root
        while current is not None:
            if data == current.data:
                # Node found, now handle deletion cases
                if current.left is None and current.right is None:  # Leaf node
                    if parent is None:
                        self.root = None
                    elif parent.left == current:
                        parent.left = None
                    else:
                        parent.right = None
                    return
                elif current.left is None:  # Node with only right child
                    if parent is None:
                        self.root = current.right
                    elif parent.left == current:
                        parent.left = current.right
                    else:
                        parent.right = current.right
                    return
                elif current.right is None:  # Node with only left child
                    if parent is None:
                        self.root = current.left
                    elif parent.left == current:
                        parent.left = current.left
                    else:
                        parent.right = current.left
                    return
                else:  # Node with two children
                    successor = self._get_successor(current)
                    self.update(successor.data, successor.data)  # Replace current with successor
                return

            elif data < current.data:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right

    def _get_successor(self, node):
        """Finds the in-order successor of a node (leftmost node in right subtree)."""
        successor = node.right
        while successor.left is not None:
            successor = successor.left
        return successor

    # Traversal methods (Inorder, Preorder, Postorder)
    def inorder(self, root):
        """Inorder traversal: left, root, right."""
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def height(self, root):
        """Calculates the height of the binary tree."""
        if root is None:
            return -1  # Height of an empty tree is -1
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return max(left_height, right_height) + 1

    def is_empty(self):
        """Checks if the binary tree is empty."""
        return self.root is None

    def minimum_value(self):
        """Finds the minimum value in the binary tree."""
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data

    def maximum_value(self):
        """Finds the maximum value in the binary tree."""
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data

    def level_order_traversal(self):
        """Performs a level-order traversal of the binary tree."""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                current_node = queue.pop(0)
                print(current_node.data, end=" ")
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            print()  # Print a newline after each level

    def inorder_successor(self, node):
        """Finds the in-order successor of a node in a BST."""
        if node is None:
            return None
        if node.right:
            return self._get_successor(node)  # Same logic as used in delete function for BST
        else:
            parent = node.parent
            while parent is not None and parent.left == node:
                node = parent
                parent = parent.parent
            return parent

    # Traversal methods (Inorder, Preorder, Postorder)
    def inorder(self, root):
        """Inorder traversal: left, root, right."""
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        """Preorder traversal: root, left, right."""
        if root is not None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        """Postorder traversal: left, right, root."""
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

