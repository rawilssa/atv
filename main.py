from random import randint

class Pessoa:
    actualyear = 2025

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birth_year(self):
        print(self.actualyear - self.age) 

    @classmethod
    def yearofbirth(cls,name,birth_year):
        age = cls.actualyear - birth_year
        return cls(name, age)

    @staticmethod
    def geraID():
        rand = randint(1,98)
        return rand

#p3 = Pessoa.yearofbirth('Rayssa', 2005)
p3 = Pessoa('rayssa',19)
print(Pessoa.geraID())
print(p3.geraID())