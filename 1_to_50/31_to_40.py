# a = '3'
# b = '4'
# print(a+b)

# print('Hi'*3)

# print('-'*80)

t1 = 'python'
t2 = 'java'
print((t1,t2)*4) # 이렇게 처리할 경우 새로운 자료형에 갇힘. +와 ,를 적절히 써줘야함
t4 = t1+t2
print(type(t4))
t3 = t1 + ' '+t2 + ' '
print(t3*4)