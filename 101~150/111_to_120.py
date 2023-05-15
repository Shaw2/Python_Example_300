# a = input('입력해보세요 : ')
# print(a*2)

# b = input('숫자지만 str링이죠. : ')
# int_b = int(b)
# print(int_b + 10)

# c = input('홀짝을 분류해드리죠 : ')
# int_c = int(c)
# if int_c%2 == 1:
#     print('홀수 입니다.')
# else :
#     print('짝수 입니다.')
    
# d = input('이진수에 갇힌 값 : ')
# int_d = int(d)
# if int_d + 20 < 255 :
#     print(int_d+20)
# else :
#     print(255)
    
# e = input('이진수에 갇힌 값 : ')
# int_e = int(e)
# # if  0 < int_e - 20 < 255 :
# #     print(int_e-20)
# # elif int_e - 20 < 0 :
# #     print(0)
# # else :
# #     print(255)
# if num > 255: # 좀 더 쉽게하려면 양극단을 빼고, 사이를 그대로 받기
#     print(255) # num = int(e) - 20
# elif num < 0:
#     print(0)
# else:
#     print(num)

# f = input('정각을 판별해주지 : ')
# # split_f = f.split(':')
# # int_f = int(split_f[1]) #
# # if int_f == 0:
# #     print('정각입니다.')
# # else :
# #     print('정각이 아닙니다.')
# if f[-2:] == "00":  # 어차피 문자열이어도 00이니까 이걸 그대로 받는게 더 빠름
#     print('정각 입니다.')
# else :
#     print('정각이 아닙니다.')

# fruit = ["사과", "포도", "홍시"]
# g = input('그 과일이 여기 있을까? : ')
# if g in fruit:
#     print('정답입니다.')
# else :
#     print('오답입니다.')

# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# h = input('조심할 종목 : ')
# if h in warn_investment_list:
#     print('투자 경고 종목입니다.')
# else:
#     print('투자 경고 종목이 아닙니다.')
    
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# keys_fruit = fruit.keys()
# i = input('계절 맞추기 : ')
# if i in keys_fruit:
#     print('정답입니다.')
# else :
#     print('오답입니다.')
    
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# values_fruit = fruit.values()
# j = input('과일 맞추기 : ') 
# if j in values_fruit:
#     print('정답입니다.')
# else :
#     print('오답입니다.')   