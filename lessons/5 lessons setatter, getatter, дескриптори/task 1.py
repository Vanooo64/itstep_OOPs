class Count:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    # якщо атрибут невизначено викликаеться метод getattr(), даний метод створенний для повернення неіснуючого значення
    def __getattr__(self, item): #item - атрибут
        print(f'Call __getatter__ {item}')


    def __getattribute__(self, item): #викликаеться кожен раз при виклику обекта, при виклику любого аргументу
        print(f'Call __getattribute__ {item}')
        if item == "version": #забороняемо доступ до якогось атибуту
            raise AttributeError ("Доступ до неіснуючого атрибуту заборонено")
        return object.__getattribute__(self, item) # викликаемо попередню почедінку __getattribute__
        # return super().__getattribute__(item) #анологічний спосіб виклику попереднї почедінки __getattribute__

    def __setattr__(self, key, value):
        print(f'Call __setater__ {key=} {value=}')
        self.__dict__[key] = value  #виконуемо присвоення (обоіязково)
        # object.__setattr__(self, key, value) #анологічний спосіб виконання присвоення (обоіязково)

    def __delattr__(self, item): #для видалення атрибуту
        print(f'Call __delater__ {item=}')
        del self.__dict__[item]


obj = Count(3, 10)

# # __delattr__
# del obj.start
# print(obj.__dict__)

# # __setattr__
# print(obj.__dict_)
# obj.version = "v1.0"
# print(obj.__dict__)

# # __getattr__
# print(obj.__dict__) #{'start': 1, 'end': 10}
# print(obj.start, obj.end)
# print(obj.version)
# print(obj.__dict__) #{'start': 1, 'end': 10}

# # def __getattribute__
# print(1, obj.start, obj.end)
# obj.version = "v1.0"
# print(obj.__dict__)
# print(obj.version)

# # __getattr__
# # def __getattribute__
# print(obj.version) #якщо атрибуту нема виликаеться __getattribute__ а він вже викликае   __getattr__ а вона по дефолту повертае None


