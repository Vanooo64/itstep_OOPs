class Task:
    def __init__(self, id, name, priority):
        self.id = id
        self.name = name
        self.priority = priority

class TaskQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, task):
        self.queue.append(task)
        self.queue.sort(key=lambda task: (task.priority, task.id))

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def completed_tasks(self):
        return len(self.queue)

# Створення черги задач
task_queue = TaskQueue()

# Додавання задач до черги
task_queue.enqueue(Task(1, "Підготувати звіт про продажі", 3))
task_queue.enqueue(Task(2, "Відправити заказ клієнту A", 1))
task_queue.enqueue(Task(3, "Сформувати презентацію для команди", 3))
task_queue.enqueue(Task(4, "Зателефонувати постачальнику щодо поставки товару", 2))
task_queue.enqueue(Task(5, "Відправити заказ клієнту B", 1))
task_queue.enqueue(Task(6, "Замовити нове обладнання для офісу", 2))

# Виконання задач у порядку
while not task_queue.is_empty():
    task = task_queue.dequeue()
    if task:
        print(f"Виконується завдання {task.id}: {task.name} (пріоритет {task.priority})")

# Виведення статистики
print(f"Виконано {task_queue.completed_tasks()} задач.")
