# def python_reverse(문자열):
#     print(문자열[::-1])
# python_reverse('python')

# def print_score(a):
#     total = 0
#     for score in a:  # sum(a) 해주면 다 더함!!
#         total +=score
#     print(total/len(a))
# print_score([3, 5, 4])

# def print_even(test_list):
#     for num in test_list:
#         if num % 2 == 0:
#             print(num)
# print_even([2, 54, 3,2,13])

# def print_keys(one_dict):
#     for key in one_dict: # one_dict.keys() 함수 사용해도 됨
#         print(key)
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})

# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
# def print_value_by_key(one_dict, date):
#     print(one_dict[date])
# print_value_by_key  (my_dict, "10/26")

# def print_5xn(sentence):
#     count = len(sentence)//5+1
#     for i in range(count):
#         i = i
#         print(sentence[0+5*i:5+5*i])    
# print_5xn("아이엠어보이유알어걸")

# def print_mxn(sentence, num):
#     count = len(sentence)//num
#     for i in range(count+1):
#         print(sentence[num*i:num+num*i])
# print_mxn("아이엠어보이유알어걸", 3)

# def calc_monthly_salary(salary):
#     monthly_salary = salary//12
#     print(monthly_salary)
# calc_monthly_salary(12000000)

# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
# my_print(a=100, b=200)

# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
# my_print(b=100, a=200)