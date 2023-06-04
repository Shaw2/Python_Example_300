class Car:
    def __init__(self, wheels, price):
        self.wheels = wheels
        self.price = price
        
    def info(self):
        print(f"바퀴수 {self.wheels}")
        print(f"가격 {self.price}")
        
# car = Car(2, 1000)
# print(car.wheels)
# print(car.price)

class Bicycle(Car):
    def __init__(self, wheels, price, motor): # 상속 받고나서 __init__이 없었을 때는 부모의 init을 쓰지만, 생기면 별도로 다 채워줘야함
        # self.wheels = wheels
        # self.price = price
        super().__init__(wheels, price) # super()를 사용하면 상속받은 클래스의 함수 사용 가능!
        self.motor = motor

    def info(self):
        super().info()
        print(f"구동계 {self.motor}")

# bicycle = Bicycle(2, 100, "시마노")

# bicycle.info()



# class 차:
#     def __init__(self, wheels, price):
#         self.wheels = wheels
#         self.price = price

# class 자동차(차):
#     def info(self):
#         print(f"바퀴수 {self.wheels}")
#         print(f"가격 {self.price}")    
        
# car = 자동차(4, 1000)
# car.info()



# class 부모:
#     def 호출(self):
#         print("부모호출")

# class 자식(부모):
#     def 호출(self):     # 매서드 오버라이딩 : 자식 클래스에서 새로 함수를 덮어쓸 수 있다는 것!
#         print("자식호출")

# 나 = 자식()
# 나.호출()

class 부모:
    def __init__(self):
        print("부모생성")

class 자식(부모):       # 상속을 한다는건 객체를 일부분 공유한다는 것! 정확히는 자식은 부모와 공유, 부모는 상관 없음
    def __init__(self):
        print("자식생성")
        super().__init__()
        
나 = 자식()