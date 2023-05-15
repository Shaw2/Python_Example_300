# inventory = {}
# inventory = {'메로나':[300, 20],
#              '비비빅':[400, 3],
#              '죠스바':[250, 100]}
# print(inventory)

# price = inventory['메로나'][0]
# print(price, '원')

# price = inventory['메로나'][1]
# print(price, '개')

# # inventory.update({'월드콘':[500, 7]})
# inventory['월드콘'] = [500, 7]
# print(inventory)

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
key_icecream = icecream.keys()
list_key_icecream = list(key_icecream)
print(type(icecream))
print(type(key_icecream))
print(list_key_icecream)

value_icecream = icecream.values()
list_value_icecream = list(value_icecream)
print(type(icecream))
print(type(value_icecream))
print(list_value_icecream)

print(sum(list_value_icecream))

new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

keys = ("apple", "pear", "peach", 'test')
vals = (300, 250, 400)
test = zip(keys, vals) # zip() 함수는 교집합의 개념으로 join을 해주는거라고 볼 수 있음
print(test)
dict_test = dict(test)
print(dict_test)
# list_test = list(test) # 리스트는 그냥 해봤는데 아무것도 안나오네
# print(list_test)
# tuple_test = tuple(test) # 튜플도 아무것도 안나옴
# print(tuple_test)

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = zip(date, close_price)
dict_c_t = dict(close_table)
print(dict_c_t)