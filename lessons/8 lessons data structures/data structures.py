#                       створення послідовності
# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return f"Node({self.data}, {str(id(self.next))[-4:]})"
#
# n1 = Node(8)
# n2 = Node(6)
# n3 = Node(4)
# n4 = Node(2)
#
# n1.next = n2
# n2.next = n3
# n3.next = n4
#
# current = n1
# while current: # поки current True
#     print(current, end=" ")
#     current = current.next


#                   Додавання у кінець списку
# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return f"Node({self.data}, {str(id(self.data))[-4:]})"
#
# class LinkedList:
#     def __init__ (self):
#         self.head = None
#
#     def append(self, data): # додае єлемент у кінець списку
#         node = Node(data)
#         if self.head is None: #якщо голова пуста, тоді значення додаеться до списку
#             self.head = node
#         else:
#             current = self.head #поточний елемент
#             while current.next: #поки current.next не None
#                 current = current.next #переміщаемо поточний елемент
#             current.next = node # коли прийшли до останнього елемента, додаемо нове значення
#
#
# lst = LinkedList()
# lst.append(8)
# lst.append(6)
# lst.append(4)
# lst.append(3)
#
#
# current = lst.head
# while current:
#     print(current, end=" ")
#     current = current.next


#                   Додавання у кінець списку з метод для виводу списку
# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return f"Node({self.data}, {self.next.data if self.next else None})"
#
# class LinkedList:
#     def __init__ (self):
#         self.head = None
#
#     def append(self, data): # додае єлемент у кінець списку
#         new_node = Node(data)
#         if self.head is None: #якщо голова пуста, тоді значення додаеться до списку
#             self.head = new_node
#         else:
#             current = self.head #поточний елемент
#             while current.next: #поки current.next не None
#                 current = current.next #переміщаемо поточний елемент
#             current.next = new_node # коли прийшли до останнього елемента, додаемо нове значення
#
#     def iter(self):  #метод для виводу списку
#         current = self.head
#         while current:
#             print(current, end=" ")
#             current = current.next
#
# lst = LinkedList()
# lst.append(8)
# lst.append(6)
# lst.append(4)
# lst.append(3)
#
# lst.iter()


# #                   Додавання перед поточним вказаним вузлом
# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return f"Node({self.data}, {self.next.data if self.next else None})"
#
# class LinkedList:
#     def __init__ (self):
#         self.head = None
#
#     def append(self, data): # додае єлемент у кінець списку
#         new_node = Node(data)
#         if self.head is None: #якщо голова пуста, тоді значення додаеться до списку
#             self.head = new_node
#         else:
#             current = self.head #поточний елемент
#             while current.next: #поки current.next не None
#                 current = current.next #переміщаемо поточний елемент
#             current.next = new_node # коли прийшли до останнього елемента, додаемо нове значення
#
#     def append_at_a_location(self, data: int, value): # додавання до позиції с парва
#         right = self.head
#         left = self.head
#         node = Node(value) #cтворюемо вузол
#         while right:
#             if right.data == data and self.head.data != data:
#                 node.next = right
#                 left.next = node
#             left = right
#             right = right.next
#
#     def iter(self):  #метод для виводу списку
#         current = self.head
#         while current:
#             print(current, end=" ")
#             current = current.next
#
# lst = LinkedList()
# lst.append(8)
# lst.append(6)
# lst.append(4)
# lst.append(3)
# lst.iter()
# print()
#
# lst.append_at_a_location(4, 5)
# lst.iter()


# #                  Видалення першого єлемента
# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return f"Node({self.data}, {self.next.data if self.next else None})"
#
# class LinkedList:
#     def __init__ (self):
#         self.head = None
#
#     def append(self, data): # додае єлемент у кінець списку
#         new_node = Node(data)
#         if self.head is None: #якщо голова пуста, тоді значення додаеться до списку
#             self.head = new_node
#         else:
#             current = self.head #поточний елемент
#             while current.next: #поки current.next не None
#                 current = current.next #переміщаемо поточний елемент
#             current.next = new_node # коли прийшли до останнього елемента, додаемо нове значення
#
#     def append_at_a_location(self, data: int, value): # додавання до позиції с парва
#         right = self.head
#         left = self.head
#         node = Node(value) #cтворюемо вузол
#         while right:
#             if right.data == data and self.head.data != data:
#                 node.next = right
#                 left.next = node
#             left = right
#             right = right.next
#
#     def delete_first_node(self): # Видалення першого єлементу списку
#         current = self.head # беремо поточний єлемент з голови
#         if self.head is None: #якщо список пустий
#             print("No data element to delete")
#         else: #
#             self.head = current.next # голоу ставимо на наступний єлемент
#
#     def iter(self):  #метод для виводу списку
#         current = self.head
#         while current:
#             print(current, end=" ")
#             current = current.next
#
# lst = LinkedList()
# lst.delete_first_node()
# lst.append(8)
# lst.append(6)
# lst.append(4)
# lst.append(3)
# lst.delete_first_node()
# lst.iter()

# #                  Видалення останнього єлемента
# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return f"Node({self.data}, {self.next.data if self.next else None})"
#
# class LinkedList:
#     def __init__ (self):
#         self.head = None
#
#     def append(self, data): # додае єлемент у кінець списку
#         new_node = Node(data)
#         if self.head is None: #якщо голова пуста, тоді значення додаеться до списку
#             self.head = new_node
#         else:
#             current = self.head #поточний елемент
#             while current.next: #поки current.next не None
#                 current = current.next #переміщаемо поточний елемент
#             current.next = new_node # коли прийшли до останнього елемента, додаемо нове значення
#
#     def append_at_a_location(self, data: int, value): # додавання до позиції с парва
#         right = self.head
#         left = self.head
#         node = Node(value) #cтворюемо вузол
#         while right:
#             if right.data == data and self.head.data != data:
#                 node.next = right
#                 left.next = node
#             left = right
#             right = right.next
#
#     def delete_first_node(self): # Видалення першого єлементу списку
#         current = self.head # беремо поточний єлемент з голови
#         if self.head is None: #якщо список пустий
#             print("No data element to delete")
#         else: #
#             self.head = current.next # голоу ставимо на наступний єлемент
#
#     def delete_last_node(self):
#         #коли є голова останній єлемент невидаляеться fix
#         current = prev = self.head
#         while current:
#             if current.next is None:
#                 prev.next = None
#             prev = current #попередній стане  current
#             current = current.next # current стане наступним
#
#
#     def iter(self):  #метод для виводу списку
#         current = self.head
#         while current:
#             print(current, end=" ")
#             current = current.next
#
# lst = LinkedList()
# lst.append(8)
# lst.append(6)
# lst.append(4)
# lst.append(3)
# lst.delete_first_node()
# lst.delete_last_node()
# lst.iter()


# #                  Видалення останнього єлемента
# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return f"Node({self.data}, {self.next.data if self.next else None})"
#
# class LinkedList:
#     def __init__ (self):
#         self.head = None
#
#     def append(self, data): # додае єлемент у кінець списку
#         new_node = Node(data)
#         if self.head is None: #якщо голова пуста, тоді значення додаеться до списку
#             self.head = new_node
#         else:
#             current = self.head #поточний елемент
#             while current.next: #поки current.next не None
#                 current = current.next #переміщаемо поточний елемент
#             current.next = new_node # коли прийшли до останнього елемента, додаемо нове значення
#
#     def append_at_a_location(self, data: int, value): # додавання до позиції с парва
#         right = self.head
#         left = self.head
#         node = Node(value) #cтворюемо вузол
#         while right:
#             if right.data == data and self.head.data != data:
#                 node.next = right
#                 left.next = node
#             left = right
#             right = right.next
#
#     def delete_first_node(self): # Видалення першого єлементу списку
#         current = self.head # беремо поточний єлемент з голови
#         if self.head is None: #якщо список пустий
#             print("No data element to delete")
#         else: #
#             self.head = current.next # голоу ставимо на наступний єлемент
#
#     def delete_last_node(self):
#         #коли є голова останній єлемент невидаляеться fix
#         current = prev = self.head
#         while current:
#             if current.next is None:
#                 prev.next = None
#             prev = current #попередній стане  current
#             current = current.next # current стане наступним
#
#
#     def iter(self):  #метод для виводу списку
#         current = self.head
#         while current:
#             print(current, end=" ")
#             current = current.next
#
#     def __len__(self): #повертае довжину списку
#         count = 0
#         current = self.head
#         while current:
#             count += 1
#             current = current.next
#         return count
#
#     def search(self, data):  #метод для пошуку значення
#         current = self.head
#         while current:
#             if current.data == data:
#                 return True
#             current = current.next
#         return False
#
#     def __contains__(self, data): #перевизначає оператор, перевіряє чи є data у методі search - (4 in lst) або lst.__contains__(4)
#         return self.search(data)
#
# lst = LinkedList()
# lst.append(8)
# lst.append(6)
# lst.append(4)
# lst.append(3)
#
#
# print(len(lst))
# print(lst.search(3))
# print(4 in lst)

#                  Ітератор у вигляді генератор функції
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data}, {self.next.data if self.next else None})"

class LinkedList:
    def __init__ (self):
        self.head = None

    def append(self, data): # додае єлемент у кінець списку
        new_node = Node(data)
        if self.head is None: #якщо голова пуста, тоді значення додаеться до списку
            self.head = new_node
        else:
            current = self.head #поточний елемент
            while current.next: #поки current.next не None
                current = current.next #переміщаемо поточний елемент
            current.next = new_node # коли прийшли до останнього елемента, додаемо нове значення

    def append_at_a_location(self, data: int, value): # додавання до позиції с парва
        right = self.head
        left = self.head
        node = Node(value) #cтворюемо вузол
        while right:
            if right.data == data and self.head.data != data:
                node.next = right
                left.next = node
            left = right
            right = right.next

    def delete_first_node(self): # Видалення першого єлементу списку
        current = self.head # беремо поточний єлемент з голови
        if self.head is None: #якщо список пустий
            print("No data element to delete")
        else: #
            self.head = current.next # голоу ставимо на наступний єлемент

    def delete_last_node(self):
        #коли є голова останній єлемент невидаляеться fix
        current = prev = self.head
        while current:
            if current.next is None:
                prev.next = None
            prev = current #попередній стане  current
            current = current.next # current стане наступним

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __next__(self):
        return self






lst = LinkedList()
lst.append(8)
lst.append(6)
lst.append(4)
lst.append(3)
for x in lst:
    print(x, end=" ")