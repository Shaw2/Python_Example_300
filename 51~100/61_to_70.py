# price = ['20180728', 100, 130, 140, 150, 160, 170]
# new_price = price[1:]
# print(new_price)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_nums = nums[::2]
# print(new_nums)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_nums = nums[1::2]
# print(new_nums)

# nums = [1, 2, 3, 4, 5]
# new_nums = nums[::-1]
# print(new_nums)

# interest = ['삼성전자', 'LG전자', 'Naver']
# #print(interest[::2])
# print(interest[0], interest[2])

# interests = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# # for interest in interests:
# #     print(interest, end=' ')
# print(" ".join(interests))

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# str_interest = "/".join(interest)
# print(str_interest)

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# line_interest = "\n".join(interest)
# print(line_interest)

# string = "삼성전자/LG전자/Naver"
# list_string = string.split('/')
# print(list_string)

# data = [2, 4, 3, 1, 5, 10, 9]
# asc_data = data.sort(reverse=True) # sort()는 재귀함수여서 리스트에 직접 영향을 줌. 
#                                    # Descending 하고 싶으면 reverse=True. 기본값은 reverse=False
# print(asc_data) #  그래서 asc_data에는 아무것도 들어가지 않는 것
# print(data)