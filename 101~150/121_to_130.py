# user_input = input('대소문자를 판별해드리죠. : ')
# if user_input.islower():
#     trans_input = user_input.upper()
#     print(trans_input)
# else:
#     trans_input = user_input.lower()
#     print(trans_input)

# score_input = int(input('점수를 입력해주세요 : '))
# if score_input <= 20:
#     grade = 'E'
# elif score_input <= 40:
#     grade = 'D'
# elif score_input <= 60:
#     grade = 'C'
# elif score_input <= 80:
#     grade = 'B'
# elif score_input <= 100:
#     grade = 'A'
# print('grade is {}'.format(grade))

# # user_input = input('환전해 드릴께요 : ')
# # split_input = user_input.split()
# # exchange_input = int(split_input[0])
# # country = split_input[1]
# # if country == '달러':
# #     dollar = exchange_input*1167
# #     print(dollar)
# # elif country == '엔':
# #     en = exchange_input*1.096
# #     print(en)
# # elif country == '유로':
# #     uro = exchange_input*1268
# #     print(uro)
# # elif country == '위안':
# #     wian = exchange_input*171
# #     print(wian)
# # else:
# #     print('정보가 없는 돈 입니다.')
# 환율 = {'달러' : 1167,
#       '엔' : 1.096,
#       '유로': 1268,
#       '위안' : 171}
# user_input = input('입력:')
# num, currency = user_input.split()  # .split()을 통해서 이와 같이 바로 할당 가능
# print(float(num)*환율[currency], '원') # currency 정보가 있으므로 이를 key로 활용

# number1 = 10
# number2 = 9
# number3 = 20
# num = [number1, number2, number3]
# print(num)
# num.sort()  # .sort()는 재귀함수!
# print(num)
# print(num[-1:])

# phone_info = {'011':'SKT',
#               '016':'KT',
#               '019':'LGU',
#               '010':'알수없음'}
# user_input = input('전화번호를 입력하세요. : ')
# first_num, sec, third = user_input.split('-') # 여기선 맨 앞에것만 받아도 무방
# print('당신은 {} 사용자입니다.'.format(phone_info[first_num]))

# post_num = {'강북구': ['0','1','2'], 
#             '도봉구' : ['3','4','5'], 
#             '노원구': ['6','7','8','9']}
# print(post_num)
# user_post = input('우편번호를 입력하세요 : ')
# post_area = user_post[2] # 원래 문제는 '앞 3자리 이므로 [:3]을 써서 푸는게 좋음
# for key, value in post_num.items():  # dict{}.items()  요거 완전 꿀!
#     # print(key)
#     # print(value)
#     if post_area in value:
#         print(key)
        
# user_num = input('주민번호를 입력하세요. : ')
# back_num = user_num.split('-')[1]
# print(back_num)
# user_sex = back_num[0]
# if user_sex == '1'or'3':
#     print('남자')
# elif user_sex == '2'or'4':
#     print('여자')
# else:
#     print('잘못 입력하셨습니다.')
    
# user_num = input('주민번호를 입력하세요 : ')
# seoul = range(0,9)    # 어차피 int로 받으니까 굳이 range를 할 필요 없이 <= 8 로도 가능 
# print(seoul)
# back_num = user_num.split('-')[1]
# area_num = back_num[1:3]
# # print(area_num)
# # print(type(area_num))
# int_area_num = int(area_num)
# # print(int_area_num)
# # print(type(int_area_num))
# if int_area_num in seoul:
#     print('서울입니다.')
# else :
#     print('서울이 아닙니다.')

# lists = ['1', '2', '6']
# int_list = int(lists) # 리스트에 있는 str들은 int로 한 번에 안바뀜
# print(int_list)

user_input = input('주민번호 유효 체크 : ')
split_user_input = user_input.split('-')
forward_num = split_user_input[0]
backward_num = split_user_input[1]
x = [2, 3, 4, 5, 6, 7, 8, 9]
print(x[-1])
a=0
forward_sum = 0
for i in forward_num:
    forward_sum = forward_sum + int(i)*x[a]
    a = a+1
print(a)
backward_sum = 0
for i in backward_num[0:-1]:
    backward_sum = backward_sum + int(i)*x[a]
    a = a+1
    print(a)
    if a >= 8:
        a = 0

first_calcul = (forward_sum+backward_sum)%11
sec_calcul = 11 - first_calcul
check_num = int(backward_num[-1])
if sec_calcul != check_num:
    print('유효하지 않은 주민등록번호입니다.')
