class Stock:
    def __init__(self, name, code, PER, PBR, 배당수익률):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.배당수익률 = 배당수익률
        
    def set_name(self, name):
        self.name = name
        
    def set_code(self, code):
        self.code = code
        
    def set_PER(self, PER):
        self.PER = PER
        
    def set_PBR(self, PBR):
        self.PBR = PBR
        
    def set_dividend(self, dividend):
        self.배당수익률 = dividend
    
    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code
        
# a = Stock(None, None)
# print(a.name)
# a.set_name("삼성전자")
# print(a.name)
# a.set_code("005930")
# print(a.code)
# print(a.get_name())
# print(a.get_code())

삼성전자 = Stock('삼성전자', "005930", 15.79, 1.33, 2.83) # 0으로 끝나는 값은 다른 처리를 하거나 우선 문자열로 넣어야함
                                                        # 안그러면 syntaxError 뜸


삼성전자.set_PER(12.75)
print(삼성전자.PER)

companies = [['삼성전자', '005930', 15.79, 1.33, 2.83],
             ['현대차', '005380', 8.70, 0.35, 4.27],
             ['LG전자', '066570', 317.34, 0.69, 1.37]]

for i in companies:
    i[0] = Stock(i[0], i[1], i[2], i[3], i[4])
    
    print(i[0].get_code())
    print(i[0].PER)