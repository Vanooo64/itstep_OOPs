import re


class NameDescriptor: #дескриптор для username, first_name, last_name
    def __init__(self, prefix, min_length, max_length, allow_chars):
        self.var = None
        self.prefix = prefix
        self.min_length = min_length
        self.max_length = max_length
        self.allow_chars = allow_chars

    def __get__(self, instance, owner):
        if self.var is None:
            return None
        return f"{self.prefix}_{self.var}"

    def __set_name__(self, owner, name):
        self.var = name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Значення повинно бути рядком")
        if not re.match("^[A-Za-z][A-Za-z0-9_-]*$", value):
            raise ValueError(f"{self.var} не задовольняє умовам")
        if not self.min_length <= len(value) <= self.max_length:
            raise ValueError(f"{self.var} повинен бути від {self.min_length} до {self.max_length} символів")
        self.var = value


class PasswordEmailDescriptor: #дескриптор для Password, Email
    def __init__(self, prefix, min_length, max_length, allow_chars, email_regex):
        self.var = None
        self.prefix = prefix
        self.min_length = min_length
        self.max_length = max_length
        self.allow_chars = allow_chars
        self.email_regex = email_regex

    def __get__(self, instance, owner):
        if self.var is None:
            return None
        return f"{self.prefix}_{self.var}"

    def __set_name__(self, owner, name):
        self.var = name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Значення повинно бути рядком")
        if not self.min_length <= len(value) <= self.max_length:
            raise ValueError(f"{self.var} повинен бути від {self.min_length} до {self.max_length} символів")
        if self.var == "email":
            if not re.match(self.email_regex, value):
                raise ValueError("Некоректний формат email")
            # Перевірка на унікальність email
            for user in instance._users:  # Зверніть увагу, що тут ми використовуємо instance
                if user is not instance and user.email == value:
                    raise ValueError("Цей email вже зареєстрований")
        self.var = value


class User:
    _users = []  # Список для зберігання всіх об'єктів User

    username = NameDescriptor("username", 5, 20, "A-Za-z0-9_-")
    first_name = NameDescriptor("first_name", 1, 50, "A-Za-z")
    last_name = NameDescriptor("last_name", 1, 50, "A-Za-z")
    password = PasswordEmailDescriptor("password", 8, 20, "A-Za-z0-9_-!@#$%^&*()[]{}", r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}")
    email = PasswordEmailDescriptor("email", 1, 50, "A-Za-z0-9_-@.", r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}")

    def __init__(self, username, first_name, last_name, email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        User._users.append(self)

    def __repr__(self):
        return f"""{self.username} 
{self.first_name}
{self.last_name}
{self.email}
{self.password}"""

# Приклад використання
user1 = User("john_doe", "John", "Doe", "john@example.com", "password123")
user2 = User("alice-123", "Alice", "Smith", "alice@example.com", "secure_pass")
print(user1)