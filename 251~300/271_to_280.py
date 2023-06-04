import random

# import time
# time = time.ctime()
# print('시간 : ', time)

from datetime import datetime
# s = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 이 방식으로 timestamp를 str으로해서 리스트에 저장 가능!
# print(s)


class Account:
    
    account_count = 0 # 클래스 안에다가 변수를 만들면 그 변수 사용을 위해서 클래스를 먼저 호출해야함
    
    def __init__(self, name, balance):
        self.bank = "SC은행"
        self.name = name
        self.balance = balance
        
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []
        
        first = random.randrange(0,999)
        second = random.randrange(0,99)
        third = random.randrange(0,999999)
        
        first_ant = str(first).zfill(3)
        second_ant = str(second).zfill(3)
        third_ant = str(third).zfill(3) # str 자료형에 .zfill 함수를 이용하면 자릿수를 채울 수 있다!
                
        self.account_number = f"{first_ant}-{second_ant}-{third_ant}"
        
        Account.account_count += 1  # 엄밀히는 안, 밖으로 나뉜 것이므로 class 변수를 부르기 위해 Account 사용
        
    # def get_account_num(): # 이건 객체가 부르는게 아니라 클래스가 부르는 것이므로 'self' 생략
    #     return Account.account_count
    
    @classmethod    # 이렇게 어노테이션을 달아놓으면 class를 self로 받아서 사용가능. 없으면 TypeError뜸
    def get_account_num(cls): # 위 어노테이션으로 인해서 class 혹은 객체를 받는 것으로 바뀜
        return cls.account_count
            
    def deposit(self, money):
        if money >= 1:
            self.balance += money
            self.deposit_count += 1
            t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.deposit_log.append(t)
            self.deposit_log.append(money)
            if self.deposit_count%5 == 0:
                self.balance *= 1.01

    def withdraw(self, money):
        if self.balance - money >= 0:
            self.balance -= money
            t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.withdraw_log.append(money)
            self.withdraw_log.append(t)
    
    def display_info(self):
        print(f"은행이름 : {self.bank}")
        print(f"예금주: {self.name}")
        print(f"계좌번호 : {self.account_number}")
        # balance = self.balance
        # p_balance = balance.split
        print(f"잔고: {self.balance:,}") # 거의 마법인데?? f"{}" 함수에 이런 기능이 들어있나보다. 대박
            
    def deposit_history(self):
        for d_his in self.deposit_log: # 함수이름과 변수 이름이 같으면 안됨!
            print(d_his)
    
    def withdraw_history(self):
        for w_his in self.withdraw_log:
            print(w_his)
    
# kim = Account("김민수", 100)
# print(kim.name)
# print(kim.balance)
# print(kim.bank)
# print(kim.account_number)
# print(Account.get_account_num())  # 이를 통해서 객체를 만들지 않아도 클래스는 그 자체로 함수를 사용할 수 있음을 알 수 있다.


# k = Account("kim", 100)
# k.deposit(100)
# k.withdraw(90)
# print(k.balance)

# p = Account("파이썬", 10000)
# p.display_info()

# p = Account("파이썬", 10000)
# p.deposit(10000)
# p.deposit(10000)
# p.deposit(10000)
# p.deposit(5000)
# p.deposit(5000)
# print(p.balance)

# account_list = []

# k = Account("kim", 10000000)
# p = Account("파이썬", 10000)
# a = Account("yabal", 5000)

# account_list.append(k)
# account_list.append(p)
# account_list.append(a)

# # print(account_list)

# for account in account_list:
#     if account.balance >= 10000000:
#         account.display_info()

k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()
        
        