import random
Lista_serv=[]
class Servidor:
    def __init__(self, nome, SIAPE, cpf, dtnasc, código_servidor=None, código_veiculo=None, descrição=None, placa=None, marca=None, modelo=None, salário=None, endereço=None, tipo=None,rg=None):
        self.código_servidor=código_servidor or random.randint(1, 500)
        self.nome=nome
        self.SIAPE=SIAPE
        self.rg=rg
        self.cpf=cpf
        self.endereço=endereço
        self.salário=salário
        self.dtnasc=dtnasc
        self.tipo=tipo
        self.descrição=descrição
        self.placa=placa
        self.marca=marca
        self.modelo=modelo
        self.código_veiculo=código_veiculo or random.randint(1,1000)
        

    def exibir_dados(self):
        if self.cpf in Lista_serv:
            servidor=Lista_serv[self.cpf]
            print(f"Código do servidor: {self.código_servidor}")
            print(f"Nome: {self.nome}")
            print(f"CPF: {self.cpf}")
            print(f"SIAPE: {self.SIAPE}")
            print(f"RG: {self.rg}")
            print(f"Endereço: {self.endereço}")
            print(f"Tipo: {self.tipo}")
            print(f"Data de nascimento: {self.dtnasc}")
            print(f"Salário: {self.salário}")
            print(f"Descrição do veículo: {self.descrição}")
            print(f"Placa do veículo: {self.placa}")
            print(f"Modelo do veículo: {self.modelo}")
            print(f"Marca do veículo: {self.marca}")
            print(f"Código do veículo: {self.código_veiculo}")

    def inserir_servidor(self, cpf):
        if self.cpf not in Lista_serv:
            Lista_serv.append(self)
            print(f"Servidor {self.nome} cadastrado com sucesso.Código do servidor: {self.código_servidor}!")
        else:
            print(f"Servidor {self.nome} ja consta no sistema.")

    def alterar_dados(self, código_servidor, nome=None, cpf=None, SIAPE=None, rg=None, endereço=None, tipo=None, dtnasc=None, salário=None):
        if self.código_servidor in Lista_serv:
            servidor=Lista_serv[self.código_servidor]
            if nome:
                 self.nome = nome
            if cpf:
                 self.cpf = cpf
            if SIAPE:
                 self.SIAPE = SIAPE
            if rg:
                 self.rg = rg
            if endereço:
                 self.endereço = endereço
            if tipo:
                 self.tipo = tipo
            if dtnasc:
                 self.dtnasc = dtnasc
            if salário:
                 self.salário = salário

    def excluir_servidor(self):
        if self.código_servidor in Lista_serv:
            Lista_serv.remove(self.código_servidor)
            print(f"Servidor {self.nome} foi removido.")
        else:
            print(f"Servidor {self.nome} não consta no sistema.")

    def dados_cod(self, código_servidor):
        for servidor in Lista_serv:
            if servidor.código_servidor == código_servidor:
                print(f"Código do servidor: {self.código_servidor}")
                print(f"Nome: {self.nome}")
                print(f"CPF: {self.cpf}")
                print(f"SIAPE: {self.SIAPE}")
                print(f"RG: {self.rg}")
                print(f"Endereço: {self.endereço}")
                print(f"Tipo: {self.tipo}")
                print(f"Data de nascimento: {self.dtnasc}")
                print(f"Salário: {self.salário}")
                print(f"Descrição do veículo: {self.descrição}")
                print(f"Placa do veículo: {self.placa}")
                print(f"Modelo do veículo: {self.modelo}")
                print(f"Marca do veículo: {self.marca}")
                print(f"Código do veículo: {self.código_veiculo}")
                return 
        print(f"nenhum servidor com {self.código_servidor} encontrado.")    

    def listar(self):
        print("TODOS OS SERVIDORES:")
        for Servidor in Lista_serv:
            print(f"{Servidor.nome}")

    def listar_ordemalfabetica(self):
        print("TODOS OS SERVIDORES EM ORDEM ALFABÉTICA:")
        servordem = sorted(Lista_serv, key=lambda s: s.nome)
        for Servidor in servordem:
            print(f"{Servidor.nome}")


s1 = Servidor("Maria castro", "23", "12345678989", "15/04/2004")
s2 = Servidor("Luana rezende", "98", "36745698723", "07/09/1983")
s3= Servidor("Ana Prado", "76", "87776543109", "26/02/1999")
s4 = Servidor("Thiago Rodrigues", "24", "65409856263", "19/06/1976")

s2.inserir_servidor("36745698723")
s3.inserir_servidor("87776543109")
s4.inserir_servidor("65409856263")
s1.inserir_servidor("12345678989")
Servidor.listar(Lista_serv)
s2.dados_cod(s2.código_servidor)
Servidor.listar_ordemalfabetica(Lista_serv)



















"""def alterar(self, Código, novo_nome, novo_siape, novo_rg, novo_cpf, novo_endereço, novo_salário, novo_dtnasc, novo_tipo):
        for servidor in self.servidores:
            if servidor.Código == Código:
                servidor.nome=novo_nome
                servidor.siape=novo_siape
                servidor.rg=novo_rg
                servidor.cpf=novo_cpf
                servidor.endereço=novo_endereço
                servidor.salário=novo_salário
                servidor.dtnasc=novo_dtnasc
                servidor.tipo=novo_tipo
                print(f"Dados do servidor {servidor.nome} alterado")
                return
            print("Servidor {servidor.nome} ainda nao cadastrado para alteração de dados")

    def listar(self):
        return [servidor.exibir_dados() for servidor in self.servidores]
    
    def listar_cod(self, Código):
        for servidor in self.servidores:
            if servidor.códigoS == Código:
                return [servidor.exibir_dados() for servidor in self.servidores]

    def listar_ordem(self):
        servidores_ordenados= sorted(self.servidores, key=lambda servidor: servidor.nome)
        for servidor in servidores_ordenados:
            print(servidor.nome)"""
