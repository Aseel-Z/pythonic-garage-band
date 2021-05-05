class Band(Musician):
    allBands=[]
    def __init__(self,name):
        self.name=name
        self.members= super().__init__(self)
        self.allBands = allBands.append(self)
    def play_solos(self):
        print('Hey {self.members}! Please play solo!')

    @classmethod
    def to_list(cls):
        return cls.allBands

    
    def __repr__(self):
       return f"Band(name={self.name}, members={self.members})"

    def __str__(self):
        separator = ', '
        string = separator.join(self.members)
       return f"The band name is:{self.name} and the members names are {string}"
        
class Musician():
    def __init__(self,name,instrument):
        self.name=name
        self.instrument=instrument
    def get_instrument(self):
        return "plays the {self.instrument}"
    def play_solo(self):
        print('Hey {self.name}! Please play solo!')

    def __repr__(self):
        return f"Musician(name={self.name}, instrument={self.instrument})"
    def __str__(self):
        return f"{self.name} is a great musician who plays the {instrument}"
        



class Guitarist(Musician):
    super().__init__(self)
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    
class Bassist(Musician):
    super().__init__(self)
        return f"Bassist instance. Name = {self.name}"
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    
class Drummer(Musician):
    super().__init__(self)
         return f"Drummer instance. Name = {self.name}"
    def __str__(self):
        return f"My name is {self.name} and I play drums"



