# 클래스, 객체, 인스턴스에 대해 설명
# 클래스 : 여러 객체

# class Human:
#     pass
        
# class Human:
#     pass
# areum = Human()

# class Human:
#     def __init__(self):
#         print('응애응애')
# areum = Human()

# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         print('응애응애')
# areum = Human("아름", 25, "여자")
# print(areum.name)

# print(areum.name)
# print(areum.age)
# print(areum.sex)

# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def who(self):
#         print(self.name)
#         print(self.age)
#         print(self.sex)
# areum = Human("아름", 25, "여자")
# areum.who() # Human.who(areum)과 동일! 지금은 self로 자기 자신을 받지만 Human class에 있는 인스턴스를 불러오는 것도 가능한 것

# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def who(self):
#         print(self.name)
#         print(self.age)
#         print(self.sex)
#     def setInfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
# areum = Human("모름", 0, "모름")
# areum.who()
# areum.setInfo("아름", 25, "여자")
# areum.who()

# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def __del__(self):
#         print("나의 죽음을 알리지마라")
#     def who(self):
#         print(self.name)
#         print(self.age)
#         print(self.sex)
#     def setInfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
        
# areum = Human("아름", 25, "여자")
# del(areum)
# areum.who()

class OMG :
    def print() :   # class를 통해서 만들었지만, self가 없어서 어떤 객체에서 이 함수를 쓰는지 모름. 그래서 error남
        print("Oh my god")

mystock = OMG()
mystock.print()      # OMG.print(mystock)  