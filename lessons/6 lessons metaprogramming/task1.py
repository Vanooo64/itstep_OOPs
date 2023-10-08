# MyClass = type('My', (), {})
#
# # class MyClass: # аналогічно
# #     pass
#
# obj = MyClass()
# print(type(obj).__name__)
# print(type(MyClass).__name__)

# MyClass = type('MyClass', (), {"username": "admin", "count": 0,})
#
# # class MyClass: # аналогічно
# #     username = "admin"
# #     count = 0
#
#
# obj = MyClass()
# print(MyClass.username)

def get_count(self):
    print('Call method get_count')
    return self.count

MyClass = type('MyClass', (), {"username": "admin", "count": 10, 'info': get_count})


# class MyClass: # аналогічно
#     username = "admin"
#     count = 0
#
#     def get_count(self):
#         print('Call method get_count')
#         return self.count




obj = MyClass()
print(obj.username)
print(obj.info())

