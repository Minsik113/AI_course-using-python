import random
from abc import ABCMeta
from abc import abstractmethod
import turtle

# Parent1 Class - Duck
class Duck(metaclass=ABCMeta):
    
    SIZE = 20
    color_list = ['blue', 'red', 'orange', 'green']
    
    def __init__(self):
        self._x = random.randint(-300, 300)
        self._y = random.randint(-300, 300)
        self.turtle = turtle
        self._flycheck = False
        self._quackcheck = False
    
    @abstractmethod
    def display(self):
        pass

    def swim(self):
        self.turtle.penup()
        self.turtle.goto(self._x - 50, self._y + 30)
        self.turtle.write("수영")
        self.turtle.pendown()
# Parent2 Class - Quack class
class Quack(metaclass=ABCMeta):
    
    @abstractmethod
    def quack(self):
        pass
# Parent3 Class - Fly class
class Fly(metaclass=ABCMeta):
    
    @abstractmethod
    def fly(self):
        pass
# Child1 Class - MallardDuck
#Child1
class MallardDuck(Duck, Quack, Fly):
    
    def __init__(self):
        super(MallardDuck, self).__init__()
        self._color = 0
        self._flycheck = True
        self._quackcheck = True
        
    #--abstract method--
    def display(self):
        print("BLUE")
        self.turtle.color(Duck.color_list[self._color])
        
        self.turtle.penup()
        self.turtle.goto(self._x, self._y)
        self.turtle.pendown()
        
        self.turtle.begin_fill()
        self.turtle.circle(self.SIZE)
        self.turtle.end_fill()
        
    def quack(self):
        self.turtle.penup()
        self.turtle.goto(self._x + 30, self._y + 30)
        self.turtle.pendown()
        self.turtle.write("꽥꽥")

    def fly(self):
        self.turtle.penup()
        self.turtle.goto(self._x - 50, self._y - 20)
        self.turtle.pendown()
        self.turtle.write("날다")

# Child2 Class - RedDuck
#Child2
class RedDuck(Duck, Quack, Fly):
    
    def __init__(self):
        super(RedDuck, self).__init__()
        self._color = 1
        self._flycheck = True
        self._quackcheck = True
        
    #--abstract method--
    def display(self):
        print("Red")
        self.turtle.color(Duck.color_list[self._color])
        
        self.turtle.penup()
        self.turtle.goto(self._x, self._y)
        self.turtle.pendown()
        
        self.turtle.begin_fill()
        self.turtle.circle(self.SIZE)
        self.turtle.end_fill()
    
    def quack(self):
        self.turtle.penup()
        self.turtle.goto(self._x + 30, self._y + 30)
        self.turtle.pendown()
        self.turtle.write("꽥꽥")

    def fly(self):
        self.turtle.penup()
        self.turtle.goto(self._x - 50, self._y - 20)
        self.turtle.pendown()
        self.turtle.write("날다")

# Child3 Class - RubberDuck
class RubberDuck(Duck, Quack):
    
    def __init__(self):
        super(RubberDuck, self).__init__()
        self._color = 2
        self._quackcheck = True

    #--abstract method--
    def display(self):
        print("ORANGE")
        self.turtle.color(Duck.color_list[self._color])
        
        self.turtle.penup()
        self.turtle.goto(self._x, self._y)
        self.turtle.pendown()
        
        self.turtle.begin_fill()
        self.turtle.circle(self.SIZE)
        self.turtle.end_fill()
        
    def quack(self):
        self.turtle.penup()
        self.turtle.goto(self._x + 30, self._y + 30)
        self.turtle.pendown()
        self.turtle.write("삑삑")

# Child4 Class - Decoy Duck
#Child4
class DecoyDuck(Duck):
    
    def __init__(self):
        super(DecoyDuck, self).__init__()
        self._color = 3
        
    #--abstract method--
    def display(self):
        print("GREEN")
        self.turtle.color(Duck.color_list[self._color])
        
        self.turtle.penup()
        self.turtle.goto(self._x, self._y)
        self.turtle.pendown()
        
        self.turtle.begin_fill()
        self.turtle.circle(self.SIZE)
        self.turtle.end_fill()

# DuckManager Class
class DuckManager:
    
    __duck_list = []
    
    def __init__(self):
        self.createDucks()
        
    def createDucks(self):
        for i in range(random.randint(1,4)):
            self.__duck_list.append(MallardDuck())
        for i in range(random.randint(1,4)):
            self.__duck_list.append(RedDuck())
        for i in range(random.randint(1,4)):
            self.__duck_list.append(RubberDuck())
        for i in range(random.randint(1,4)):
            self.__duck_list.append(DecoyDuck())
    
    def displayAllDucks(self):
        for duck in DuckManager.__duck_list:
            if duck != None:
                duck.display()
                duck.swim()
                if isinstance(duck, Quack):
                    duck.quack()
                if isinstance(duck, Fly):
                    duck.fly()

if __name__ == "__main__":
    md = DuckManager()
    md.displayAllDucks()