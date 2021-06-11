class Duck :
    
    # instance value
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__color = ''
    
    # decorator 
    @property
    def color(self): 
        return self.__color

    @color.setter
    def color(self, col): 
        self.__color = col

    def display(self):
        print(self.__color,'Duck의 현재위치는 (', self.__x, ',', self.__y, ') 입니다.')

    def move(self, x, y):
        self.__x = x 
        self.__y = y

    def sound(self):
        print("꽥!")

duck1 = Duck()
duck1.display()
duck1.color = "Red"
duck1.move(3,3)
duck1.sound()
duck1.display()

duck2 = Duck()
duck2.display()
duck2.color = 'Mallard'
duck2.move(1,5)
duck2.sound()
duck2.display()
