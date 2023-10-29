class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, data): # Додавання елемента до списку в голову.
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_to_tail(self, data):  # Додавання елемента до списку в голову.
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_from_head(self): #Видалення елемента зі списку з голови.
        if not self.head:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_from_tail(self): # Видалення елемента зі списку з хвоста)
        if not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete_by_value(self, value): #видалення елемента за значенням
        current = self.head
        while current:
            if current.data == value:
                if current == self.head:
                    self.delete_from_head()
                elif current == self.tail:
                    self.delete_from_tail()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next

    def add_by_index(self, data, index): #додавання нового елемента за індексом.
        if index == 0:
            self.add_to_head(data)
        else:
            current = self.head
            current_index = 1
            while current_index < index and current:
                current = current.next
                current_index += 1
            if current_index == index:
                new_node = Node(data)
                new_node.prev = current.prev
                new_node.next = current
                current.prev.next = new_node
                current.prev = new_node

    def traverse_forward(self): #Прохід по всьому списку від голови до хвоста
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def traverse_backward(self): #Прохід по всьому списку від хвоста до голови.
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

    def clear(self): #Повне очищення списку.
        self.head = None
        self.tail = None

    def display(self):  # метод для відображення списку
        current = self.head  # визначаемо перший єлемент списку поточним
        while current:  # поки current не = None
            print(current.data, end=" -> ")
            current = current.next  # переміщуемо current на наступний єлемент
        print("None")

lst = DoublyLinkedList()
# #тест додавання у голову
# lst.add_to_head(1)
# lst.add_to_head(2)
# lst.add_to_head(3)
# lst.display()

# #тест додавання у хвіст
# lst.add_to_tail(1)
# lst.add_to_tail(2)
# lst.add_to_tail(3)
# lst.add_to_tail(4)
# lst.display()

# #тест видалення
# lst.add_to_tail(1)
# lst.add_to_tail(2)
# lst.add_to_tail(3)
# lst.add_to_tail(4)
# lst.delete_from_head()
# lst.delete_from_tail()
# lst.display()

# # тест видалення елемента за значенням
# lst.add_to_tail(1)
# lst.add_to_tail(2)
# lst.add_to_tail(3)
# lst.add_to_tail(4)
# lst.delete_by_value(3)
# lst.display()

# # тест додавання нового елемента за індексом.
# lst.add_to_tail(1)
# lst.add_to_tail(2)
# lst.add_to_tail(3)
# lst.add_to_tail(4)
# lst.add_by_index(11,2)
# lst.display()

# # тест прохід по всьому списку від голови до хвоста.
# lst.add_to_tail(1)
# lst.add_to_tail(2)
# lst.add_to_tail(3)
# lst.add_to_tail(4)
# lst.traverse_forward()
#
#
# # тест прохід по всьому списку від хвоста до голови.
# lst.traverse_backward()

# тест повне очищення списку.
lst.add_to_tail(1)
lst.add_to_tail(2)
lst.add_to_tail(3)
lst.add_to_tail(4)
lst.display()
lst.clear()
lst.display()



