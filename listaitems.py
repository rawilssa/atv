
class Item:
    def __init__(self):
        self.item = {}

    def ins_item(self, nome, valor):
        if ('Itens') not in self.item:
            self.item['Itens'] ={nome:valor}
        else:
            self.item['Itens'].update({nome:valor})

    def editaitem(self,nome,valor):
        if (self,nome,valor) not in self.item:
            print('O item não existe para ser editado.')
        else:
            self.item['Itens'].update({nome:valor})

    def lista(self):
        for nome, valor in self.item['Itens'].items():
            print(nome, valor)

    def apagitem(self,nome,valor):
        if (self,nome,valor) not in self.item:
            print('O item não existe para ser deletado.')
        else:
            del self.item['Itens'][nome]

Itm = Item()
Itm.apagitem('arroz', 8)
Itm.ins_item('arroz', 6)
Itm.ins_item('arroz', 6)
Itm.editaitem('agua', 3)
print(Itm.item)