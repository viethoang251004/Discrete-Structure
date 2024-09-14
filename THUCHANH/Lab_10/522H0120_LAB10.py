from collections import deque
# Ex1
def print_level_order(tree):
    if isinstance(tree, list):
        root = build_tree_from_vector(tree)
        queue = deque([root])
    else:
        if not tree:
            return
        queue = deque([tree])
    while queue:
        level_size = len(queue)
        level_values = []
        for _ in range(level_size):
            node = queue.popleft()
            if node is not None:
                level_values.append(node.data if hasattr(node, 'data') else node)
                if hasattr(node, 'left'):
                    queue.append(node.left)
                if hasattr(node, 'right'):
                    queue.append(node.right)
            else:
                level_values.append(None)
        print([node if node else None for node in level_values])
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def build_tree_from_vector(tree_vector):
    if not tree_vector:
        return None
    root = TreeNode(tree_vector[0])
    queue = deque([root])
    i = 1

    while queue and i < len(tree_vector):
        node = queue.popleft()
        if tree_vector[i] is not None:
            node.left = TreeNode(tree_vector[i])
            queue.append(node.left)
        i += 1
        if i < len(tree_vector) and tree_vector[i] is not None:
            node.right = TreeNode(tree_vector[i])
            queue.append(node.right)
        i += 1

    return root
left_tree = [2, 7, 5, 2, 6, None, 5, 11, 4]
right_tree = [50, 17, 76, 9, 23, 54, 9, 14, 19, 12, None, 72, 67]
print("Exercise 1: Represent the trees as Vector of values and print out each level in separate line")
print("\nLeft Tree:")
print_level_order(left_tree)
print("\nRight Tree:")
print_level_order(right_tree)
# Ex2
left_tree_root = build_tree_from_vector(left_tree)
right_tree_root = build_tree_from_vector(right_tree)
print("\nExercise 2: Represent the binary trees using linked list")
print("\nLeft Tree:")
print_level_order(left_tree_root)
print("\nRight Tree:")
print_level_order(right_tree_root)
# Ex3
def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")
print("\nExercise 3: Traversals")
print("\nPreorder (Left Tree): ", end="")
preorder(left_tree_root)
print("\nInorder (Left Tree): ", end="")
inorder(left_tree_root)
print("\nPostorder (Left Tree): ", end="")
postorder(left_tree_root)
print("\n\nPreorder (Right Tree): ", end="")
preorder(right_tree_root)
print("\nInorder (Right Tree): ", end="")
inorder(right_tree_root)
print("\nPostorder (Right Tree): ", end="")
postorder(right_tree_root)
# Ex4
def breadth_first_search(root, data):
    if not root:
        return
    queue = deque([root])
    path = []
    while queue:
        node = queue.popleft()
        path.append(node.data)
        if node.data == data:
            return path
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None
def depth_first_search(root, data):
    if not root:
        return None
    stack = [(root, [root.data])]
    while stack:
        node, path = stack.pop()
        if node.data == data:
            return path
        if node.right:
            stack.append((node.right, path + [node.right.data]))
        if node.left:
            stack.append((node.left, path + [node.left.data]))
    return None
print("\nExercise 4: Breadth First Search")
print("Path to find 11 in Left Tree (linked list):", breadth_first_search(left_tree_root, 11))
print("Path to find 19 in Right Tree (linked list):", breadth_first_search(right_tree_root, 19))
print("\nExercise 4: Depth First Search")
print("Path to find 11 in Left Tree (linked list):", depth_first_search(left_tree_root, 11))
print("Path to find 19 in Right Tree (linked list):", depth_first_search(right_tree_root, 19))
# Ex5
def breadth_first_search_vector(tree, data):
    if not tree:
        return None
    queue = deque([(tree, 0)])
    path = []
    while queue:
        node, index = queue.popleft()
        if node is not None:
            path.append(node)
            if node == data:
                return path
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            if left_index < len(tree):
                queue.append((tree[left_index], left_index))
            if right_index < len(tree):
                queue.append((tree[right_index], right_index))
    return None
print("\nExercise 5: Breadth First Search (Vector)")
print("Path to find 11 in Left Tree (vector):", breadth_first_search_vector(left_tree, 11))
print("Path to find 19 in Right Tree (vector):", breadth_first_search_vector(right_tree, 19))