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

phone_info = {'011':'SKT',
              '016':'KT',
              '019':'LGU',
              '010':'알수없음'}
user_input = input('전화번호를 입력하세요. : ')
first_num, sec, third = user_input.split('-') # 여기선 맨 앞에것만 받아도 무방
print('당신은 {} 사용자입니다.'.format(phone_info[first_num]))