
class Produto:
    def __init__(self,nome,preço):
        self.nome = nome
        self.preço = preço

    def desconto(self,percentual):
        self.preço = self.preço - (self.preço * (percentual / 100)) 

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,valor):
        self._nome = valor.replace('S','@' )

    # getter
    @property
    def preço(self):
        return self._preço
    
    # setter
    @preço.setter
    def preço(self,valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$',''))
        self._preço = valor


p1 = Produto('BLUSA', 40)
p2 = Produto('VESTIDO', 114)
p3 = Produto('SAIA', 'R$42')
print(p1.nome, p1.preço)
p3.desconto(10)
print(p3.nome,p3.preço)