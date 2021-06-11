import random

class StudentInfo :
#     def __new__(cls) :
#         print('new')
#         obj = super().__new__(cls)
#         return obj
        
    def __init__(self) :
        self.__haknum = random.randint(1,100)
        self.__kor = random.randint(1,100) # __kor는 private임
        self.__math = random.randint(1,100)
        self.__eng = random.randint(1,100)
        self.__total = self.__kor + self.__eng + self.__math
    
    ##########################################
    ################ decorator ###############
    ##########################################
    @property
    def haknum(self): # getter
        return self.__haknum
    
    @haknum.setter 
    def haknum(self, num):
        if num >= 0:
            self.__haknum = num
    
    @property
    def kor(self): # getter
        return self.__kor

    @kor.setter
    def kor(self, score): # setter
        if score > 0:
            self.__kor = score
    
    @property
    def eng(self): # getter
        return self.__eng
    
    @eng.setter
    def eng(self, score):
        if score > 0:
            self.__eng = score
    
    @property
    def math(self): # getter
        return self.__math
    
    @math.setter
    def math(self, score):
        if score > 0:
            self.__math = score
    
    def setTotal(self):
        self.__total = self.__kor + self.__math + self.__eng
        
    def display(self):
        self.setTotal()
        print(self.__kor, '+', self.__eng, '+', self.__math, '=', self.__total)
    
    
s1 = StudentInfo()
s1.display()
s1.kor = 40 
s1.math = 40
s1.eng = 40
s1.display()