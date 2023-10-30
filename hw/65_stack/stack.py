# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class Stack:
#     def __init__(self, max_size=-1):
#         self.top = None
#         self.max_size = max_size
#         self.size = 0
#
#     def push(self, data):
#         """додавання рядка у стек"""
#         if self.is_full():
#             print("Стек переповнений.")
#         else:
#             new_node = Node(data)
#             if self.top:
#                 new_node.next = self.top
#             self.top = new_node
#             self.size += 1
#
#     def pop(self):
#         """Виштовхнути рядок із стеку"""
#         if self.is_empty():
#             print("Стек порожній.")
#             return None
#         data = self.top.data
#         self.top = self.top.next
#         self.size -= 1
#         return data
#
#     def is_empty(self):
#         """Перевірити чи порожній стек"""
#         return self.size == 0
#
#     def is_full(self):
#         """Перевірити чи повний стек"""
#         return self.max_size != -1 and self.size >= self.max_size
#
#     def size_stec(self):
#         """підрахунок кількості рядків у стеку (розмір стеку) – size"""
#         return self.size
#
#     def clear(self):
#         """повне очищення стеку """
#         self.top = None
#         self.size = 0
#
#     def peek(self):
#         """отримання значення без виштовхування верхнього рядка зі стеку """
#         if self.is_empty():
#             print("Стек порожній.")
#             return None
#         return self.top.data
#
#
# # Меню для тестування
# stack = Stack()
# while True:
#     print("Меню:")
#     print("1. Додати рядок у стек")
#     print("2. Виштовхнути рядок із стеку")
#     print("3. Перевірити чи порожній стек")
#     print("4. Перевірити чи повний стек")
#     print("5. Отримати розмір стеку")
#     print("6. Повністю очистити стек")
#     print("7. Подивитися верхній рядок стеку без виштовхування")
#     print("0. Вийти з програми")
#
#     choice = input("Виберіть опцію: ")
#
#     if choice == "1":
#         data = input("Введіть рядок, який потрібно додати: ")
#         stack.push(data)
#     elif choice == "2":
#         popped_data = stack.pop()
#         if popped_data is not None:
#             print(f"Виштовхнуто: {popped_data}")
#     elif choice == "3":
#         if stack.is_empty():
#             print("Стек порожній.")
#         else:
#             print("Стек не порожній.")
#     elif choice == "4":
#         if stack.is_full():
#             print("Стек повний.")
#         else:
#             print("Стек не повний.")
#     elif choice == "5":
#         print(f"Розмір стеку: {stack.size_stec()}")
#     elif choice == "6":
#         stack.clear()
#         print("Стек очищено.")
#     elif choice == "7":
#         top_data = stack.peek()
#         if top_data is not None:
#             print(f"Верхній рядок стеку: {top_data}")
#     elif choice == "0":
#         break


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None


def check_brackets(input_string):
    stack = Stack()

    for char in input_string:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.is_empty():
                return False  # Знайшли закриваючу дужку без відповідної відкриваючої
            stack.pop()  # Видаляємо відповідну відкриваючу дужку

    # Після перевірки всіх символів у рядку, стек повинен бути порожнім
    return stack.is_empty()


# Приклади виклику функції для тестування:
print(check_brackets("((()))"))  # Результат: True, рядок містить правильну розстановку дужок
print(check_brackets("(()()())"))  # Результат: True, рядок містить правильну розстановку дужок
print(check_brackets("((())"))  # Результат: False, рядок містить неправильну розстановку дужок
print(check_brackets("())("))  # Результат: False, рядок містить неправильну розстановку дужок
