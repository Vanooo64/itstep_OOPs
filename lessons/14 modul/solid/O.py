import os
from abc import ABC,abstractmethod
class IOutput(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def display(self):
        pass

class ConsoleOutput(IOutput):

    def display(self):
        print(f"{self.data}")


class FileOutput(IOutput):

    def display(self):
        with open('output1.txt', 'w') as f:
            f.write(self.data)


obj = ConsoleOutput("some string_to_file")
obj.display()

obj_to_file = FileOutput('some string_to_file22222')
obj_to_file.display()
