import random
from abc import ABCMeta
from abc import abstractmethod
import turtle

#Parent
class Duck(metaclass=ABCMeta):
    
    SIZE = 20
    color_list = ['blue', 'red', 'orange', 'green']
    
    def __init__(self):
        self._x = random.randint(-300, 300)
        self._y = random.randint(-300, 300)
        self._color = -1
        self.turtle = turtle
    
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def swim(self):
        pass

#Child1
class MallardDuck(Duck):
    
    def __init__(self):
        super(MallardDuck, self).__init__()
        self._color = 0
    
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
    
    def swim(self):
        self.turtle.penup()
        self.turtle.goto(self._x - 50, self._y + 30)
        self.turtle.write("수영")
        self.turtle.pendown()

for i in range(2):
    ml = MallardDuck()
    if ml != None:
        ml.display()
        ml.swim()
        ml.quack()
        ml.fly()

# ml = MallardDuck()
# ml.display()
# ml.swim()
# ml.quack()
# ml.fly()