# def 함수(문자열) :
#     print(문자열)
# 함수("안녕")
# 함수("Hi")

# def 함수(a, b) :
#     print(a + b)
# 함수(3, 4)
# 함수(7, 8)

# def 함수(a:int, b:int) :
#     print(a + b)
# 함수("안녕", 3)

# def print_with_smile(문자열:str):
#     print(f'{문자열}:D')
    
# print_with_smile('안녕하세요')
    
# def print_upper_price(c_price):
#     print(c_price*1.3)
# print_upper_price(100)

# def print_sum(a, b):
#     print(a+b)
# print_sum(3, 6)

# def print_arithmetic_operation(a, b):
#     print(f'{a} + {b} = {a+b}')
#     print(f'{a} - {b} = {a-b}')
#     print(f'{a} * {b} = {a*b}')
#     print(f'{a} / {b} = {a/b}')
# print_arithmetic_operation(3, 4)

def print_max(a, b, c):
    # if a>b and a>c:
    #     print(a)
    # elif b>a and b>c:
    #     print(b)
    # elif c>b and c>a:
    #     print(c)
    max_val = 0
    if a > max_val : # 이런식으로 만드는게 계산도 적게 들어가고 좋군!
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)
print_max(15, 5, 13)