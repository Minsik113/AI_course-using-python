class Student() :
    def __init__(self, st_id, name):
        self.__st_id = st_id
        self.__name = name
        self.__kor = 0
        self.__eng = 0
        self.__math = 0

    def setKor(self, kor) :
        self.__kor = kor
    def setEng(self, eng) :
        self.__eng = eng
    def setMath(self, math) :
        self.__math = math
        
    def getKor() :
        return self.__kor
    def getEng() :
        return self.__eng
    def getMath() :
        return self.__math
    def getTotal() :
        total = self.__kor + self.__eng + self.__math
        return total

    def display(self) :
        print('학번:',self.__st_id, '이름:',self.__name, '국어:',self.__kor, '영어:',self.__eng, '수학:',self.__math, '총점:',self.getTotal())
        # print('학번:',self.__st_id)
        # print('이름:',self.__name)
        # print('국어:',self.kor)
        # print('영어:',self.eng)
        # print('수학:',self.math)
        # print('총점:',self.getTotal())

st1 = Student(1,'홍길동')
st1.setKor(25)
st1.setEng(34)
st1.setMath(56)
st1.display()
# print()
st2 = Student(2,'김길동')
st2.setKor(56)
st2.setEng(78)
st2.setMath(34)
st2.display()
# print()
st3 = Student(3,'이길동')
st3.setKor(78)
st3.setEng(56)
st3.setMath(78)
st3.display()