class Node: #клас вершини

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"


class Tree:
    def __init__(self, root: Node):
        self.root = root

    def preorder(self, start, trace):
        "Root  -> Left -> Right"
        if start:
            trace = trace + str(start.value) + "--"
            trace = self.preorder(start.left, trace)
            trace = self.preorder(start.right, trace)
        return trace

    def postorder(self, start, trace):
        "Left -> Right -> Root"
        if start is not None:
            trace = self.preorder(start.left, trace)
            trace = self.preorder(start.right, trace)
            trace = trace + str(start.value) + "--"
        return trace

    # def add_node(self, parent_value, new_node_value, type = "left"):
    #     "Додання значення у листки"
    #     parent_nada = self.find_parent_by_value(node=self.root, parent_value)

    def find_parent_by_value(self, node, value):
        if  node.value == value:
            return node
        if node.left:
            node = self.find_parent_by_value(node.left, value)
        elif node.right:
            node = self.find_parent_by_value(node.right, value)
        return node

    def insert(self, value):
        pass


5 3 2 4 7 6 8

#              5
#          /       \
#       3             7
#     /   \        /    \
#   2      4     6       8





#              1
#          /       \
#       2             3
#     /   \             \
#   4      5            6

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.right = Node(6)

#              1
#          /       \
#       2             3
#     /   \             \
#   4      5             6

root = Node(1)
tree = Tree(root)

print(tree.root)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(6)

# print(tree.preorder(tree.root, trace=""))
# print(tree.postorder(tree.root, trace=""))

print(tree.find_parent_by_value(node=tree.root, value=6))

