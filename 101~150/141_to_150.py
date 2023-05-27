# 리스트 = [100, 200, 300]
# for price in 리스트 :
#     print(price+10)

# 리스트 = ["김밥", "라면", "튀김"]
# for 음식 in 리스트:
#     print("오늘의 메뉴:", 음식)

# 리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
# for enterp in 리스트:
#     print(len(enterp))

# 리스트 = ['dog', 'cat', 'parrot']
# for animal in 리스트:
#     spell_count = len(animal)
#     print(animal, spell_count)

# 리스트 = ['dog', 'cat', 'parrot']
# for animal in 리스트:
#     first_spell = animal[:1]
#     print(first_spell)

# 리스트 = [1, 2, 3]
# for number in 리스트:
#     print(리스트[2], 'x {}'.format(number))
    
# 리스트 = [1, 2, 3]
# for number in 리스트:
#     print(f'3 x {number} =', 3*number)

# 리스트 = ["가", "나", "다", "라"]
# for 문자 in 리스트[1:]:
#     print(문자)

# 리스트 = ["가", "나", "다", "라"]
# for 문자 in 리스트[0::2]:
#     print(문자)

리스트 = ["가", "나", "다", "라"]
for 문자 in 리스트[::-1]:
    print(문자)