# def n_plus_1 (n) :
#     result = n + 1
# n_plus_1(3)
# print (result)

# def make_url(name):
#     return f'www.{name}.com'
# print(make_url('naver'))

# def make_list(texts):
#     # tong = []
#     # for text in texts:
#     #     tong.append(text)
#     # return tong
#     return list(texts) # 문자열을 list로 형변환 해줘도 빠르게 수행 가능
# print(make_list("abcd"))

# def pickup_even(one_list):
#     even = []
#     for num in one_list:
#         if num%2 == 0:
#             even.append(num)
#     return even
# print(pickup_even([3, 4, 5, 6, 7, 8]))

# def convert_int(string_num):
#     # nums = string_num.split(',')
#     # a = ''
#     # for num in nums:
#     #     a = a+num
#     # int_a = int(a)    
#     # return int_a
#     return int(string_num.replace(',', '')) # .replace()가 있었지!!
# print(convert_int("1,234,567"))

# def 함수(num) :
#     return num + 4
# a = 함수(10)
# b = 함수(a)
# c = 함수(b)
# print(c)

# def 함수(num) :
#     return num + 4
# c = 함수(함수(함수(10)))
# print(c)

# def 함수1(num) :
#     return num + 4
# def 함수2(num) :
#     return num * 10
# a = 함수1(10)
# c = 함수2(a)
# print(c)

# def 함수1(num) :
#     return num + 4
# def 함수2(num) :
#     num = num + 2
#     return 함수1(num)
# c = 함수2(10)
# print(c)

# def 함수0(num) :
#     return num * 2
# def 함수1(num) :
#     return 함수0(num + 2)
# def 함수2(num) :
#     num = num + 10
#     return 함수1(num)
# c = 함수2(2)
# print(c)