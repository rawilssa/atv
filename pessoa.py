from datetime import datetime 

class Pessoa:
    actual_year = datetime.strftime(datetime.now(), '%Y')
    def __init__(self, name, age, eating=False, talking=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.talking = talking

    def talk(self, topic):
        if self.eating:
            print(f'{self.name} não pode falar comendo.')
            return
        
        if self.talking:
            print(f'{self.name} ja está falando.')
            return
        
        print(f'{self.name} está falando sobre {topic}.')
        self.talking = True
    
    def stop_talk(self):
        if not self.talking:
            print(f'{self.name} não está falando.')
            return
        
        print(f'{self.name} parou de falar.')
        self.talking = False


    def eat(self,food):
        if self.eating:
            print(f'{self.name} ja está comendo.')
            return
        if self.talking:
            print(f'{self.name} não pode comer falando.')
            return
        
        print(f'{self.name} esta comendo {food}!') 
        self.eating = True
    
    def stop_eat(self):
        if not self.eating:
            print(f'{self.name} não esta comendo.')
            return
        

        print(f'{self.name} parou de comer.')
        self.eating = False
    
    def birth_year(self):
        return self.actual_year - self.age