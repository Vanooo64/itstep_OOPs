from abc import ABC, abstractmethod

class BinarySearchTre(ABC):
    def __init__(self, root=None):
        self.root = root

    @abstractmethod
    def insert(self, value):
        pass

    @abstractmethod
    def remove(self, value):
        pass

    @abstractmethod
    def find_min(self):
        pass

    @abstractmethod
    def search(self, value):
        pass

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"

class MyBinarySearchTree(BinarySearchTre):
    def __init__(self, root=None):
        super().__init__(root)

    def insert(self, value):
        # Реалізація вставки вузла в дерево
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node

    def remove(self, value):
        # Реалізація видалення вузла з дерева
        self.root = self._remove(self.root, value)

    def _remove(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._remove(node.left, value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.value = self._find_min(node.right).value
            node.right = self._remove(node.right, node.value)
        return node


    def find_min(self):
        # Реалізація пошуку мінімального значення в дереві
        return self._find_min(self.root).value if self.root else None

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def search(self, value):
        # Реалізація пошуку вузла за значенням в дереві
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

    def inorder(self):
        trace = ""
        trace = self.inorder_recursive(self.root, trace)
        return trace

    def inorder_recursive(self, start, trace):
        if start:
            trace = self.inorder_recursive(start.left, trace)
            trace = trace + str(start.value) + " -- "
            trace = self.inorder_recursive(start.right, trace)
        return trace

    def __str__(self):
        return self.inorder()

# #3. Створення та побудова бінарного дерева пошуку
# bst = MyBinarySearchTree()
#
# values = [12, 19, 8, 4, 10, 5, 21, 11, 15, 9, 1, 14, 16]
#
# for value in values:
#     bst.insert(value)
#
# # Виведення дерева
#
# def print_tree(node, level=0, prefix="Root: "):
#     if node is not None:
#         print(" " * (level * 4) + prefix + str(node.value))
#         if node.left is not None or node.right is not None:
#             print_tree(node.left, level + 1, "L--- ")
#             print_tree(node.right, level + 1, "R--- ")
#
# print_tree(bst.root)

# # 4. Створення та побудова бінарного дерева пошуку
# bst = MyBinarySearchTree()
# values = [12, 19, 8, 4, 10, 5, 21, 11, 15, 9, 1, 14, 16]
#
# for value in values:
#     bst.insert(value)
#
# # Пошук значення в дереві
#
# search_value = 10
# result_node = bst.search(search_value)
#
# # Виведення результатів
#
# if result_node:
#     print(f"Значення {search_value} знайдено в дереві.")
# else:
#     print(f"Значення {search_value} не знайдено в дереві.")

# #5. Створення та побудова бінарного дерева пошуку
# bst = MyBinarySearchTree()
#
# values = [12, 19, 8, 4, 10, 5, 21, 11, 15, 9, 1, 14, 16]
#
# for value in values:
#     bst.insert(value)
#
# # Знаходження мінімального значення в дереві
#
# min_value = bst.find_min()
#
# # Виведення результатів
#
# if min_value is not None:
#     print(f"Мінімальне значення в дереві: {min_value}")
# else:
#     print("Дерево порожнє.")

# 6. Створення та побудова бінарного дерева пошуку
bst = MyBinarySearchTree()
values = [12, 19, 8, 4, 10, 5, 21, 11, 15, 9, 1, 14, 16]

for value in values:
    bst.insert(value)

# Відображення дерева до видалень
print("Дерево до видалень:")
print(bst)

# Покрокове видалення вузлів
nodes_to_remove = [11, 10, 12]

for value in nodes_to_remove:
    bst.remove(value)
    print(f"\nВидалено вузол {value}:")
    print(bst)