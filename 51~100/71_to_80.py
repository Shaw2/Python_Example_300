# my_variable = ()
# print(type(my_variable))

# movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
# print(movie_rank)

# num = (1, )
# print(type(num), num)

# lists = [1, 2, 3]
# lists[0] = 3
# print(lists) # 리스트는 이처럼 변경이 가능하지만 튜플은 변경 안됨

# t = 1, 2, 3, 4
# print(type(t)) # 원칙적으로는 () 안에 써야하지만 편의를 위해 없이도 사용 가능

# t = ('a', 'b', 'c')
# t = ('A', 'b', 'c')

# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# list_interest = list(interest)
# print(list_interest)

# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# tuple_interest = tuple(interest)
# print(tuple_interest)

# temp = ('apple', 'banana', 'cake')
# a, b, c= temp # , d가 하나 더 있으면 valueError 발생
# print(a, b, c) # 튜플과 변수가 매칭된다면 다음과 같이 하나씩 나옴

# jjack = tuple(range(2, 99, 2)) # range() 함수는 range라는 자료형을 갖는다. 따라서 tuple()로 변환해줘야 함!
#                                # range는 이터러블 
# print(jjack)

# https://codingalzi.github.io/pybook/casestudy_collections.html