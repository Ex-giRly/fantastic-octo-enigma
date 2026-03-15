from abc import ABC, abstractmethod

class ABSClass(ABC):


    def display(self, x):
        print("passed value: ", x)


        @abstractmethod
        def task(self):
            print("we are inside ABSClass task")

class TestClass(ABSClass):
    def task(self):
        print("We are inside TestClass task")

obj = TestClass()
obj.task
obj.display(100)