class Servidor:
    def __init__(self, codigoS, nome, siape, CPF, datanasc):
        self.serv = {}
        self.codigos = codigoS
        self.nome = nome
        self.siape = siape
        self.CPF = CPF
        self.datanasc = datanasc

    def regserv(self, codigoS, nome, siape, CPF, datanasc):
        if ('serv') not in self.serv:
            self.serv['serv'] ={codigoS, nome, siape, CPF, datanasc}
        else:
            self.serv['serv'].update({codigoS, nome, siape, CPF, datanasc})
            
    def exibir(self):
        print(f"codigoS: {self.codigos}")
        print(f"nome: {self.nome}")
        print(f"siape: {self.siape}")
        print(f"CPF: {self.CPF}")
        print(f"datanascimento: {self.datanasc}")

    def apagserv(self, CPF):
        if (self, CPF) not in Servidor:
            print('O servidor não existe para ser deletado.')
        else:
            del self.serv['serv'][nome]
            print(f'{self.nome} foi deletado do sistema.')

Servidor1 = Servidor(1,'Maria', 456, 14575683244, 15102001)
Servidor1.apagserv(14575683244)




























class Veiculo:
    def __init__(self, codigoV, modelo, descricao, placa, marca):
        self.codigov = codigoV
        self.modelo = modelo
        self.descricao = descricao
        self.placa = placa
        self.marca = marca
        self.modelo = modelo

