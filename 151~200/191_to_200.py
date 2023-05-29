# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# for row in data:
#     for price in row:
#         print(price+(price*0.00014)) # %이므로 .00이 더 들어감 # price*1.00014로 해도 동일

# for row in data:
#     for price in row:
#         print(price+(price*0.00014))
#     print('----')

# results = []
# for row in data:
#     for price in row:
#         result = price*1.00014
#         results.append(result)
# print(results)

# results = []
# for row in data:
#     a = []
#     for price in row:
#         result = price*1.00014
#         a.append(result)
#     results.append(a)
# print(results)

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for row in ohlc:
#     if type(row[3]) == int :
#         print(row[3])
        
# for row in ohlc[1:]:
#     if row[3] > 150:
#         print(row[3])
        
# for row in ohlc[1:]:
#     if row[3] >= row[0]:
#         print(row[3])

# volatility = []
# for row in ohlc[1:]:
#     gap = row[1]-row[2]
#     volatility.append(gap)
# print(volatility)

# for row in ohlc[1:]:
#     if row[3] > row[0]:
#         print(row[1]-row[2])

# get_money = 0
# for row in ohlc[1:]:
#     get_money += row[3] - row[0]
# print(get_money)