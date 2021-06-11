import random
from abc import *
import turtle

# Parent Class
class Duck(metaclass=ABCMeta):
    #static variable
    SIZE = 30
    color_list = ['blue', 'red']

    #instance value
    def __init__(self):
        self._x = random.randint(-300, 300)
        self._y = random.randint(-300, 300)
        self.turtle = turtle
        self._color = -1

    # @abstractmethod
    def display(self):
        self.turtle.penup()
        self.turtle.goto(self._x, self._y)
        self.turtle.pendown()
        
        self.turtle.color(Duck.color_list[self._color])
        self.turtle.begin_fill()
        self.turtle.circle(self.SIZE)
        self.turtle.end_fill()
        
        self.turtle.penup()
        self.turtle.pendown()
        self.turtle.write("move\t\tquack")  #print text

    def sound(self):
        print('quack')
        self.turtle.penup()
        self.turtle.goto(self._x - 50, self._y + 50)
        self.turtle.pendown()
        self.turtle.write("quack")

    def move(self):
        print('move')
        self.turtle.penup()
        self.turtle.goto(self._x + 30, self._y + 50)
        self.turtle.pendown()
        self.turtle.write("move")

    def screen_reset(self):
        self.turtle.reset()

# Child Class1
class MallardDuck(Duck):
    def __init__(self):
        super(MallardDuck, self).__init__()
        self._color = 0

    #override Method
    def display(self):
        self.turtle.color(Duck.color_list[self._color])
        
        self.turtle.penup()
        self.turtle.goto(self._x, self._y)
        self.turtle.pendown()

        self.turtle.begin_fill()
        self.turtle.circle(self.SIZE)
        self.turtle.end_fill()

# Child Class2
class RedDuck(Duck):
    
    def __init__(self):
        super(RedDuck, self).__init__()
        self._color = 1

    #override Method
    def display(self):
        self.turtle.color(Duck.color_list[self._color])
        
        self.turtle.penup()
        self.turtle.goto(self._x, self._y)
        self.turtle.pendown()

        self.turtle.begin_fill()
        self.turtle.circle(self.SIZE)
        self.turtle.end_fill()    

class DuckManager:

    def __init__(self):
        self.__duck_list = []
        self.__nmallard = 0
        self.__nred = 0

    def createDucks(self, nmallard, nred):
        self.__nmallard = nmallard
        self.__nred = nred

        for i in range(self.__nmallard):
            self.__duck_list.append(MallardDuck())
        for i in range(self.__nred):
            self.__duck_list.append(RedDuck())
    
    def displayAllDucks(self):
        for v in self.__duck_list:
            if v != None:
                v.display()
                v.move()
                v.sound()

    def deleteDucks(self):
        for v in self.__duck_list:
            v.screen_resert()

if '__main__':
    manager = DuckManager()
    manager.createDucks(5,5)
    manager.displayAllDucks()
    manager.deleteDucks()
        
