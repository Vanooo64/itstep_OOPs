class Ten:
    def __get__(self, instance, owner): #self - обект дескриптора, instance - обект , owner - клас)
        print(f"{instance} - {owner}")
        return instance.__dict__['xxx'] # аналогічно instance.xxx   аналогічно       #getattr(instance, "xxx") підтягуе з сетера

    def __set__(self, instance, value):
        print(f"{self} - {instance} - {value}")
        if value > 0:
            instance.xxx = value

class A:
    x = 5
    y = Ten() # дискриптор

a = A()

# __set__
a.y = 20
print(a.__dict__)



# # __get__
# print(a.x)
# print(a.y)
