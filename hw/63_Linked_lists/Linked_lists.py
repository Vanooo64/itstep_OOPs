class Node:
    def __init__(self, data=None):
        self.data = data #значення списку
        self.next = None # посилання на наступне значення


class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None

    def append(self, data):
        """додае єлемент у кінець списку"""
        new_node = Node(data)
        if self.head is None: #якщо голова пуста, тоді значення додаеться до списку
            self.head = new_node
        else:
            current = self.head #поточний елемент
            while current.next: #поки current.next не None
                current = current.next #переміщаемо поточний елемент
            current.next = new_node # коли прийш

    def add_to_head(self, data):
        """Додати елемент до списку на початок"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, target_data, data):
        """Вставити новий елемент із деяким значенням безпосередньо після елемента із даними, що є у списку"""
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == target_data:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def delete_last_node(self):
        """Видалити елемент з хвоста списку"""
        if not self.head: #якшо список потожній, нічого неповертаемо
            return
        if not self.head.next: #Якщо у списку є лише один елемент, то він видаляється шляхом призначення
            self.head = None
            return

        current = self.head # ніціалізуємо змінну current значенням self.head, щоб почати перебір списку з початку.
        while current.next.next: #продовжуватися, поки current має наступний елемент після поточного.
            current = current.next #У кожній ітерації циклу ми переходимо до наступного елементу

        current.next = None #Коли цикл завершується, ми призначаємо None останньому вузлу

    def delet_first_node(self):
        """Видалити елемент з голови списку"""
        current = self.head
        if self.head is None:
            print('Немає элементів для видалення')
        else:
            self.head = current.next

    def delete_value(self, target_data, delete_all=False):
        """Видалити елемент із деяким значенням у списку (задається яке значення та кількість можливих видалень, бо у списку дані можуть повторюватись). """
        if not self.head:
            return
        while self.head and self.head.data == target_data:
            self.head = self.head.next

        current = self.head
        while current and current.next:
            if current.next.data == target_data:
                current.next = current.next.next
                if not delete_all:
                    break
            else:
                current = current.next

    def replace_value(self, old_data, new_data, replace_all=False):
        """Замінити значення у списку на нове значення (користувач визначає, чи замінити тільки перше входження чи всі)"""
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                if not replace_all:
                    break
            current = current.next

    def size(self):
        """Визначте розмір списку"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


    def display(self):  #метод для відображення списку
        current = self.head #визначаемо перший єлемент списку поточним
        while current:      # поки current не = None
            print(current.data, end=" -> ")
            current = current.next # переміщуемо current на наступний єлемент
        print("None")


my_list = LinkedList() #створюємо список


def display_menu():
    print()
    print("Меню:")
    print("1. Додати елемент у хвіст списку")
    print("2. Додати елемент до списку на початок")
    print("3. Вставити новий елемент після певного значення")
    print("4. Видалити елемент з хвоста списку")
    print("5. Видалити елемент з голови списку")
    print("6. Видалити елемент за значенням")
    print("7. Замінити значення в списку")
    print("8. Визначити розмір списку")
    print("9. Показати вміст списку")
    print("0. Вийти")


while True:
    display_menu()
    choice = int(input("Виберіть опцію: "))

    if choice == 1:
        value = input("Введіть елемент, який Ви хочете додати у хвіст списку: ")
        my_list.append(value)
    elif choice == 2:
        value = input("Введіть елемент, який Ви хочете додати у голову списку: ")
        my_list.add_to_head(value)
    elif choice == 3:
        value = input("Введіть значення, після якого потрібно вставити новий елемент: ")
        new_element = input("Введіть новий елемент: ")
        my_list.insert_after(value, new_element)
    elif choice == 4:
        my_list.delete_last_node()
        print(f'Отанній елемент видалено з списку')
    elif choice == 5:
        my_list.delet_first_node()
        print(f'Перший елемент видалено з списку')
    elif choice == 6:
        value = input("Введіть значення для видалення: ")
        delete_all = input("Видалити всі входження цього значення? (y/n): ").lower()
        my_list.delete_value(value, delete_all == 'y')
    elif choice == 7:
        old_data = input("Введіть старе значення: ")
        new_data = input("Введіть нове значення: ")
        replace_all = input("Замінити всі входження цього значення? (y/n): ").lower()
        my_list.replace_value(old_data, new_data, replace_all == 'y')
    elif choice == 8:
        print(f"Розмір списку = {my_list.size()}")
    elif choice == 9:
        print(f"Вміст списку: {my_list.display()}")
    elif choice == '0':
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
