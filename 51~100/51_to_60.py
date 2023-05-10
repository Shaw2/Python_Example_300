# movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
# print(movie_rank)

# movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
# movie_rank.append('배트맨')
# print(movie_rank)

# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank.insert(1, '슈퍼맨')
# print(movie_rank)

# #movie_rank.remove('럭키')
# del movie_rank[3]
# print(movie_rank)

# # movie_rank.remove('배트맨', '스플릿') # 이렇게는 안됨
# # del movie_rank[2, 3] # 이렇게도 안 됨. 하나씩 지워줘야함.
# del movie_rank[2]
# del movie_rank[2]
# print(movie_rank)

# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", 'C#']

# # lang1.append(lang2) # append는 리스트를 한 단위로 넣어버림
# # lang1 = lang1 + lang2 # 이렇게 2개의 리스트를 더해줘도 됨
# lang1.extend(lang2)
# print(lang1)

# nums = [1,2,3,4,5]
# # sum = 0
# # for num in nums:
# #     sum = sum + num 
# # print(sum)
# print(sum(nums))

# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
# #print(count(cook)) # 이런 함수는 없다 ㅋㅋ
# print(len(cook))

# nums = [1,2,3,4,5]
# # print(avg(nums)) # 이런 함수도 없다..!
# avg = sum(nums) / len(nums)
# print(avg)