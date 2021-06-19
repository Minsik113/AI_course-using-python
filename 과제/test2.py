from abc import abstractmethod
from abc import ABCMeta
import random

class Duck(metaclass=ABCMeta):
    
    SIZE = 30
    color_list = ['blue','red','orange','green']

    def __init__(self):
        self._x = random.randint(-300, 300)
        self._y = random.randint(-300, 300)
    
    def swim(self):
        print('수영')
    
    @abstractmethod
    def display(self):
        pass

class Fly(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

class Quack(metaclass=ABCMeta):
    @abstractmethod
    def quack(self):
        pass

class MallardDuck(Duck, Quack, Fly):
    
    def __init__(self):
        super(MallardDuck, self).__init__()
        self.__color = 0

    #--abstractmethod
    def display(self):
        print(Duck.color_list[self.__color])
    
    def quack(self):
        print("꽥꽥")
    def fly(self):
        print('날다')

class RedDuck(Duck, Quack, Fly):
    def __init__(self):
        super(RedDuck, self).__init__()
        self.__color = 1

    #--abstractmethod
    def display(self):
        print(Duck.color_list[self.__color])
    
    def quack(self):
        print("꽥꽥")
    def fly(self):
        print('날다')

class RubberDuck(Duck, Quack):
    def __init__(self):
        super(RubberDuck, self).__init__()
        self.__color = 2

    #--abstractmethod
    def display(self):
        print(Duck.color_list[self.__color])
    
    def quack(self):
        print("삑삑")
    
class DecoyDuck(Duck):
    def __init__(self):
        super(DecoyDuck, self).__init__()
        self.__color = 3

    #--abstractmethod
    def display(self):
        print(Duck.color_list[self.__color])

class DuckManager:
    
    __duck_list = []

    def __init__(self):
        self.createDucks()

    def createDucks(self):
        for i in range(random.randint(1,3)):
            self.__duck_list.append(MallardDuck())
        for i in range(random.randint(1,3)):
            self.__duck_list.append(RedDuck())
        for i in range(random.randint(1,3)):
            self.__duck_list.append(RubberDuck())
        for i in range(random.randint(1,3)):
            self.__duck_list.append(DecoyDuck())
    def displayAllDucks(self):
        for duck in DuckManager.__duck_list:
            if duck != None:
                duck.display()
    def allAttributeDucks(self):
        for duck in DuckManager.__duck_list:
            if duck != None:
                duck.display()
                duck.swim()
                if isinstance(duck, Fly):
                    duck.fly()
                if isinstance(duck, Quack):
                    duck.quack()

md = DuckManager()
md.allAttributeDucks()