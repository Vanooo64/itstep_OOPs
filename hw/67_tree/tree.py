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


    def find_parent_by_value(self, node, value):
        if  node.value == value:
            return node
        if node.left:
            node = self.find_parent_by_value(node.left, value)
        elif node.right:
            node = self.find_parent_by_value(node.right, value)
        return node


    def inorder(self):
        "Left -> Root -> Right"
        trace = ""
        trace = self.inorder_recursive(self.root, trace)
        return trace

    def inorder_recursive(self, start, trace):
        if start:
            trace = self.inorder_recursive(start.left, trace)
            trace = trace + str(start.value) + " -- "
            trace = self.inorder_recursive(start.right, trace)
        return trace

    def find_node(self, node, value):
        """
        Пошук вузла за його значенням у піддереві із коренем node.
        Якщо вузол знайдено, повертає його, інакше повертає None.
        """
        if node is None:
            return None

        if node.value == value:
            return node

        left_result = self.find_node(node.left, value)
        if left_result:
            return left_result

        right_result = self.find_node(node.right, value)
        return right_result

root = Node("A")
tree = Tree(root)

print(tree.root)
tree.root.left = Node("B")
tree.root.right = Node("C")
tree.root.left.left = Node("D")
tree.root.left.right = Node("E")
tree.root.right.right = Node("G")
tree.root.right.left = Node("F")
tree.root.right.right.right = Node("J")
tree.root.left.left.left = Node("H")
tree.root.left.left.right = Node("I")

# print("PreOrder:", tree.preorder(tree.root, ""))
# print("InOrder:", tree.inorder())
# print("PostOrder:", tree.postorder(tree.root, ""))
#
# # Приклади обходу дерева:
# # PreOrder = ABDHIECFGJ
# # InOrder = HDIBEAFCJG
# # PostOrder = HIDEBFJGCA

# Протестуємо пошук вузла зі значенням 'F' у піддереві з коренем 'A'
found_node = tree.find_node(tree.root, 'F')

if found_node:
    print(f"Знайдений вузол: {found_node}")
else:
    print("Вузол з таким значенням не знайдено.")

