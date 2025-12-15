class Node:
    """Class to represent an individual node in the BST."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# A simple BST class for initialization and insertion
class BST:
    """Class to represent a Binary Search Tree (BST)."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Inserts a new key into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        """Helper function for recursive insertion."""
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)

# =======================================================
# TASK 1: Find the Maximum Value (Max)
# =======================================================
def find_max_value(root):
    """
    Finds the largest value in the BST.
    The largest element is always the rightmost node.
    """
    if root is None:
        return None  # Handle an empty tree

    current = root
    while current.right is not None:
        current = current.right
        
    return current.key

# =======================================================
# TASK 2: Find the Minimum Value (Min)
# =======================================================
def find_min_value(root):
    """
    Finds the smallest value in the BST.
    The smallest element is always the leftmost node.
    """
    if root is None:
        return None  # Handle an empty tree

    current = root
    while current.left is not None:
        current = current.left
        
    return current.key

# =======================================================
# TASK 3: Calculate the Sum of All Values (Sum)
# =======================================================
def calculate_sum(root):
    """
    Recursively calculates the sum of all values in the tree.
    Uses a Depth-First Search (DFS) traversal approach.
    """
    if root is None:
        return 0
    
    # Sum = current node's key + sum of left subtree + sum of right subtree
    return (
        root.key + 
        calculate_sum(root.left) + 
        calculate_sum(root.right)
    )

# =======================================================
# TESTING AND EXECUTION
# =======================================================

if __name__ == '__main__':
    # Create and populate the BST
    bst = BST()
    elements = [50, 30, 70, 20, 40, 60, 80]
    for el in elements:
        bst.insert(el)
        
    print("--- BST Functions Testing ---")
    
    # Task 1
    max_val = find_max_value(bst.root)
    print(f"Maximum value found: {max_val} (Expected: 80)")
    
    # Task 2
    min_val = find_min_value(bst.root)
    print(f"Minimum value found: {min_val} (Expected: 20)")
    
    # Task 3
    total_sum = calculate_sum(bst.root)
    # Sum: 50+30+70+20+40+60+80 = 350
    print(f"Sum of all values: {total_sum} (Expected: 350)")

    # Testing with an empty tree
    empty_bst = BST()
    print("\n--- Testing Empty Tree ---")
    print(f"Max: {find_max_value(empty_bst.root)}")
    print(f"Min: {find_min_value(empty_bst.root)}")
    print(f"Sum: {calculate_sum(empty_bst.root)}")