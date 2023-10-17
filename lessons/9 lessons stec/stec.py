class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class Steck:

    def __init__(self, max_size = -1):
        self.head = None
        self.max_size = max_size # визначає розмір стеку

    # def size(self):
    #     return (self.max_size += 1)

    def push(self, data):
        if self.max_size == 0:      # якщо стейк переповнений
            raise Exception ("Стек переповнений")
        node = Node(data)
        if self.head is None:       # якщо стек порожні
            self.head = node        #голову призначаемо ноді
        else:
            node.next = self.head   #якщо нема посилання на наступний обект, призначаемо голову ноді
            self.head = node        #перевизначаемо ноду
        self.max_size -= 1

    def pop(self):
        if self.is_empty():            #перевірямо чи порожня голова
            raise ValueError("Стек порожній")
        else:
            value = self.head.data          #звертаемось до голови (ноди)
            self.head = self.head.next      #переміщаемо голову на попередне місце і голова видаляеться збірником мусору
            self.max_size += 1              # збільшуемо розмір max_size
            return value

    def is_empty(self): #якщо голова порожня повертае None
        return self.head is None

    def iter(self):
        current = self.head
        while current:
            if current.next is None:
                print(current, end=" ")
                break
            print(current, "->", end=" ")
            current = current.next

    def peak(self): # повертае значення голови
        if self.is_empty():
            raise ValueError ("Стек порожній")
        else:
            value = self.head.data
            return value



stack = Steck(max_size=3)

# stack.push(5) #додавання
# stack.push(6)
# print(stack.peak()) #повертае значення голови
# stack.push(7)
# stack.iter()
# print()
# print(stack.pop()) #видалення
# stack.iter()

stack.push(5)
stack.push(6)
stack.push(7)
stack.iter()
stack.push(8)


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class Queue:

    def __init__(self, max_size = -1):
        self._head = None
        self._tall = None
        self._size = 0

    def enqueue(self, data):            #додае з кінц (_tall), забираемо з голови (_head)
        node = Node(data)
        if self._size == 0:             #якщо черга порожня призначаемо хвіст і голову
            self._head = self._tall = node
        else:                           # додаемо єлемент в кінець
            self._tall.next = node      # беремо старий хвіст, має посилатися на Node
            self._tall = node           # новим єлементом стае Node
            self._size += 1

    def dequeue(self):  #виключити з черги
        if self._size == 0:
            raise IndexError
        node = self._head
        self._head = node.next
        self._size -= 1             #зменшуемо розмір черги
        if self._size == 0:
            self._tall = None
        return node.data

    @property
    def size(self): #повертае розмір
        return self._size

    def iter(self):
        current = self._head
        while current:
            if current.next is None:
                print(current, end=" ")
                break
            print(current, "->", end=" ")
            current = current.next


queue = Queue()
queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(1)
queue.enqueue(7)
queue.iter()



