class humans:
    def __init__(self, gender, gene, name, height, kg, persnerity='bright'):
        self.head = 1
        self.body = 1
        self.gender = gender
        self.gene = gene        
        self.name = name
        self.height = height
        self.weight = kg
        self.persnerity = persnerity
        
    def get_info(self):
        return self.persnerity

human = humans('male', 'XY', "Lee", 34, 4.3)

print(human.get_info())
