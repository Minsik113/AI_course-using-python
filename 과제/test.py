import random
from abc import *
import turtle

#Parent Class
class Duck:

    #static variable
    SIZE = 30
    color_list = ['blue','red']

    #instance value
    def __init__(self):
        self._x = random.randint(-300,300)
        self._y = random.randint(-300,300)
        self._turtle = turtle
        self._color = 0 #mallard=0, red=1
    
    @abstractmethod
    def display(self):
        pass

    def move(self):
        self._turtle.penup()
        self._turtle.goto(self._x - 50, self._y + 50)
        self._turtle.write('move')
        self._turtle.pendown()

    def sound(self):
        self._turtle.penup()
        self._turtle.goto(self._x + 50, self._y + 50)
        self._turtle.write('quack')
        self._turtle.pendown()

    def screen_reset(self):
        self._turtle.reset()

#Child Class
class MallardDuck(Duck):
    
    def __init__(self):
        super(MallardDuck, self).__init__() # python2.x
        self._color = 0

    def display(self):
        self._turtle.color(Duck.color_list[self._color])

        self._turtle.penup()
        self._turtle.goto(self._x, self._y)
        self._turtle.pendown()

        self._turtle.begin_fill()
        self._turtle.circle(self.SIZE)
        self._turtle.end_fill()

#Child Class
class RedDuck(Duck):
    
    def __init__(self):
        super(RedDuck, self).__init__()
        self._color = 1

    def display(self):
        self._turtle.color(Duck.color_list[self._color])

        self._turtle.penup()
        self._turtle.goto(self._x, self._y)
        self._turtle.pendown()

        self._turtle.begin_fill()
        self._turtle.circle(self.SIZE)
        self._turtle.end_fill()

#DuckManager Class
class DuckManager:
    def __init__(self):
        self.__duck_list = []
    
    def createDucks(self, nmallard, nred):
        for i in range(nmallard):
            self.__duck_list.append(MallardDuck())
        for i in range(nred):
            self.__duck_list.append(RedDuck())

    def displayAllDucks(self):
        for v in self.__duck_list:
            if v != None:
                v.display()
                v.move()
                v.sound()

    def deleteDucks(self):
        for v in self.__duck_list:
            v.screen_reset()

if __name__ == "__main__":
    dmanager = DuckManager()
    dmanager.createDucks(5,5)
    dmanager.displayAllDucks()
    dmanager.deleteDucks()
