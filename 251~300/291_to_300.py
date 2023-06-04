import os

# f = open('C:/Users/admin/VscodeProjects/Python_Example_300/매수종목1.txt', mode='wt', encoding='utf-8')
# f.write("005930\n")
# f.write("005380\n")
# f.write("035420\n")
# f.close()

# f = open('C:/Users/admin/VscodeProjects/Python_Example_300/매수종목2.txt', mode='wt', encoding='utf-8')
# f.write("005930 삼성전자\n")
# f.write("005380 현대차\n")
# f.write("035420 NAVER\n")
# f.close()

import csv

# f = open('C:/Users/admin/VscodeProjects/Python_Example_300/매수종목1.csv', mode='wt', encoding='cp949', newline='')
# writer = csv.writer(f)
# writer.writerow(["종목명", "종목코드", "PER"])
# writer.writerow(["삼성전자", "005930", "15.59"])
# writer.writerow(["NAVER", "035420", "55.82"])
# f.close()

# f = open("C:/Users/admin/VscodeProjects/Python_Example_300/매수종목1.txt", mode='r', encoding="utf-8")
# p = f.readlines()

# lines = []
# for line in p:
#     clean_line = line.strip()
#     lines.append(clean_line)
# print(lines)

# f = open("C:/Users/admin/VscodeProjects/Python_Example_300/매수종목2.txt", mode='r', encoding="utf-8")
# p = f.readlines()
# print(p)
# dicts = {}
# for line in p:
#     # clean_line = line.split() # .split()도 알아서 \n이 사라지네
#     # dicts[clean_line[0]] = clean_line[1]

#     k, v = line.split() # .split()으로 이런식으로 인덱스 바로 받을 수 있음
#     dicts[k] = v
    
# print(dicts)
# f.close()



# per = ["10.31", "", "8.00"]

# float_PER = []
# for i in per:
#     try:
#         float_per = float(i)
#         float_PER.append(float_per)
    
#     except:
#         print(0)
    
#     # finally: # 한 번 돌때마다 나오는구나
#     #     print(0)
# print(float_PER)


# a = 32
# try :
#     b = a/0

# except ZeroDivisionError as e:
#     print('이거냐 짜샤')
#     print('숫자를 0으로 나눌 수 없습니다.', e)


# data = [1, 2, 3]

# try:
#     for i in range(5):
#         print(data[i])
# except IndexError as e:
#     print("인덱스 범위를 벗어났습니다.", e)


per = ["10.31", "", "8.00"]

a = 0

for i in per:
    try:    
        print(float(i))
        
    except ValueError as e:
        print("넌 빈칸이 실수가 되니?", e)
        
    else :
        print("Tranfer to float is done.")
        
    finally :
        a += 1
        print(f'anyway it is turn {a} time')