class Produto:
    def __init__(self, nome, valor, marca):
        self.nome = nome
        self.valor = valor
        self.marca = marca

p1 = Produto('Blusa', 89, 'renner')
p2 = Produto('Calça', 120, 'Levis')
p3 = Produto('Casaco', 250, 'riachuelo')
p4 = Produto('Short', 75, 'Levis')
print(p1.valor)
print(p1.marca)
print(p2.nome)
print(p4.marca)