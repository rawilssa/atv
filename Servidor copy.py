class Servidor:
    def __init__(self, nome, SIAPE, rg, cpf, endereço, salário, dtnasc, tipo, codigo =None):
        self.nome = nome
        self.SIAPE=SIAPE
        self.rg=rg
        self.cpf=cpf
        self.endereço=endereço
        self.salário=salário
        self.dtnasc=dtnasc
        self.tipo=tipo
        self.codigo=codigo
        self.veiculos = []
    
class Veiculo:
    def __init__(self, codigo, descricao, placa, marca, modelo):
        self.codigo = codigo
        self.descricao = descricao
        self.placa = placa
        self.marca = marca
        self.modelo = modelo



class Sistema:
    def __init__(self, servidores = []):
        self.servidores: list = servidores
        self.index = 1
        
    técnicos = []
    professores = []
    
    def adicionar_servidor(self):
        nome = input("digite o nome completo:")
        cpf = input("digite o cpf(11 digitos):")

        if any(s.cpf == novo_servidor.cpf for s in self.servidores):
            print(f"Servidor {novo_servidor.nome} não pode ser adicionado, pois já consta no sistema.")
        else:
        
            rg = input("digite o rg:")
            SIAPE = input("digite o SIAPE:")
            endereço = input("digite o endereço:")
            salário = input("digite o salário:")
            dtnasc = input("digite a data de nascimento(dd/mm/aa):")
            tipo = input("digite o tipo(Docente ou Técnico Administrativo):")
            novo_servidor = Servidor(nome=nome, SIAPE=SIAPE, rg=rg, cpf=cpf, endereço=endereço, salário=salário, dtnasc=dtnasc, tipo=tipo, codigo=self.index)
            self.index += 1
            self.servidores.append(novo_servidor)
            print(f"Servidor {novo_servidor.nome} adicionado no sistema.")


    def alterar_servidor(self, servidor_novo: Servidor):
        Servidor.cpf = input("digite o cpf(11 digitos):")
        if Servidor in self.servidores:
            if  Servidor.cpf == servidor_novo.cpf:
                Servidor.nome = servidor_novo.nome
                Servidor.SIAPE = servidor_novo.SIAPE
                Servidor.rg = servidor_novo.rg
                Servidor.cpf = servidor_novo.cpf
                Servidor.endereço = servidor_novo.endereço
                Servidor.salário = servidor_novo.salário
                Servidor.dtnasc = servidor_novo.dtnasc
                Servidor.tipo = servidor_novo.tipo
                Servidor.codigo = servidor_novo.codigo
                print(f"Dados do servidor {Servidor.nome} alterados no sistema.")
        else:
            print(f"Servidor com CPF {servidor_novo.cpf} não encontrado no sistema.")


    def excluir_servidor(self, servidor: Servidor):
        if servidor in self.servidores:
            self.servidores.remove(servidor)
            print(f"Servidor {servidor.nome} removido do sistema.")
        else:
            print(f"Servidor {servidor.nome} não pode ser removido porque não está registrado no sistema.")


    def dadoserv_cod(self, servidor:Servidor):
        for servidor in self.servidores:
            if servidor.codigo ==self.index:
                print(f"Nome: {servidor.nome}\nSIAPE: {servidor.SIAPE}\nRG: {servidor.rg}\nCPF:{servidor.cpf}\nEndereço:{servidor.endereço}\nSalário:{servidor.salário}\nData de nascimento:{servidor.dtnasc}\nTipo:{servidor.tipo}")
            return
        print(f"Servidor {servidor.nome} não encontrado.")


    def listar_servidores(self):
        for servidor in self.servidores:
            print(f"Servidor: {servidor.nome}")


    def listar_ordalf(self):
        self.servidores.sort(key=lambda s:s.nome)
        for servidor in self.servidores:
            print(f"Servidor: {servidor.nome}")


    def listarprof_ordalf(self):
        docentes = []
        for servidor in self.servidores:
            if servidor.tipo== "Docente":
                docentes.append(servidor)
                docentes.sort(key=lambda d:d.nome)
                print("Docentes:")
                for d in docentes:
                    print(f" {d.nome}.")
    

    def listartecadm_ordalf(self):
        técnicos = []
        for servidor in self.servidores:
            if servidor.tipo== "Técnico administrativo":
                técnicos.append(servidor)
                técnicos.sort(key=lambda t:t.nome)
                print("Técnicos:")
                for t in técnicos:
                    print(f" {t.nome}.")

    def adicionar_veiculo(self, codigo):
        servidor_encontrado=None
        for servidor in self.servidores:
            if servidor.codigo == codigo :
                servidor_encontrado = servidor
                break
        if servidor_encontrado:
            marca = input("digite a marca:")
            modelo = input("digite o modelo:")
            descricao = input("digite a descrição:")
            placa = input("digite o placa:")
            novo_veiculo = Veiculo(codigo=self.index, descricao=descricao, placa=placa, marca=marca, modelo=modelo)
            servidor_encontrado.veiculos.append(novo_veiculo)
            print(f"Veículo com {codigo} adicionado com sucesso ao servidor {servidor_encontrado.nome}.")
            self.index += 1
        else:
            print(f"Servidor com o código {codigo} não encontrado no sistema.")

    def alterar_veiculo(self):

        codigo_digitado = int(input("Digite o código do veículo: "))
        veiculo_encontrado = None
        servidor_dono = None

    # Procurar o veículo em todos os servidores
        for servidor in self.servidores:
            for veiculo in servidor.veiculos:
                if novo_veiculo.codigo == codigo_digitado:
                    veiculo_encontrado = veiculo
                    servidor_dono = servidor
                    break
            if veiculo_encontrado:
                break

        if veiculo_encontrado:
            print(f"Veículo encontrado no servidor {servidor_dono.nome}.")
            nova_marca = input("Digite a nova marca: ")
            novo_modelo = input("Digite o novo modelo: ")
            nova_descricao = input("Digite a nova descrição: ")
            nova_placa = input("Digite a nova placa: ")

            veiculo_encontrado.marca = nova_marca
            veiculo_encontrado.modelo = novo_modelo
            veiculo_encontrado.descricao = nova_descricao
            veiculo_encontrado.placa = nova_placa

            print(f"Veículo com código {codigo_digitado} alterado com sucesso.")
        else:
            print(f"Veículo com código {codigo_digitado} não encontrado.")


sistema =Sistema()

sistema.adicionar_servidor()
sistema.adicionar_veiculo(1)
sistema.alterar_veiculo()
#sistema.alterar_servidor()
sistema.listar_servidores()

