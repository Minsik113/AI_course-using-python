from abc import ABCMeta
from abc import abstractmethod
import turtle, random

class Duck(metaclass=ABCMeta):
    
    SIZE = 20
    color_list = ['blue', 'red', 'yellow', 'green']

    def __init__(self):
        self._x = random.randint(-300, 300)
        self._y = random.randint(-300, 300)
        self._flycheck = False
        self._quackcheck = False
        self.turtle = turtle

    @abstractmethod
    def display(self):
        pass

    def swim(self):
        self.turtle.penup()
        self.turtle.goto(self._x - 50, self,_y + 30)
        self.turtle.write("수영")
        self.turtle.pendown()

class Quack(metaclass=ABCMeta):
    @abstractmethod
    def quack(self):
        pass

class Fly(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

class MallardDuck(Duck, Quack, Fly):
    
    def __init__(self):
        super(MallardDuck, self).__init__()
        self._color = 0
        self._flycheck = True
        self._quackcheck = True
    
    #--abstract method--
    def display(self):
        self.turtle.color(Duck.color_list[self._color])
        
        self.turtle.penup()
        self.goto(self._x, self._y)
        self.turtle.pendown()

        self.turtle.begin_fill()
        self.turtle.circle(self.SIZE)
        self.turtle.end_fill()
    
    def quack(self):
        self.turtle.penup()
        self.turtle.goto(self._x + 30, self._y + 30)
        self.turtle.write("꽥꽥")
        self.turtle.pendown()

    def fly(self):
        self.turtle.penup()
        self.turtle.goto(self._x - 50, self._y - 20)
        self.turtle.write("날다")
        self.turtle.pendown()

class RedDuck(Duck, Quack, Fly):
    pass
class RubberDuck(Duck, Quack):
    pass
class DecoyDuck(Duck):
    pass

class DuckManager:
    __duck_list = []

    def __init__(self):
        self.createDucks()

    def createDucks(self):
        pass
    def displayAllDucks(self):
        pass

if __name__ == "__main__":
    dm = DuckManager()