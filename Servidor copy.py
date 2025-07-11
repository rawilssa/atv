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
    def __init__(self, servidores = None):
        self.servidores = servidores if servidores is not None else []
        self.index = 1
        
    técnicos = []
    professores = []


    def menu_principal(self):
        while True:
            print("\n    MENU PRINCIPAL    ")
            print("1. Adicionar servidor")
            print("2. Alterar servidor")
            print("3. Excluir servidor")
            print("4. Consultar servidor por CPF")
            print("5. Listar todos os servidores")
            print("6. Listar servidores em ordem alfabética")
            print("7. Listar docentes em ordem alfabética")
            print("8. Listar técnicos em ordem alfabética")
            print("9. Adicionar veículo a um servidor")
            print("10. Sair")

            opcao = input("Digite a opção desejada: ")

            match opcao:
                case "1":
                    self.adicionar_servidor()
                case "2":
                    self.alterar_servidor()
                case "3":
                    cpf = input("Digite o CPF do servidor a ser excluído: ")
                    servidor = next((s for s in self.servidores if s.cpf == cpf), None)
                    if servidor:
                        self.excluir_servidor(servidor)
                    else:
                        print("Servidor não encontrado.")
                case "4":
                    cpf = input("Digite o CPF do servidor: ")
                    servidor = next((s for s in self.servidores if s.cpf == cpf), None)
                    if servidor:
                        self.dadoserv_cod(servidor)
                    else:
                        print("Servidor não encontrado.")
                case "5":
                    self.listar_servidores()
                case "6":
                    self.listar_ordalf()
                case "7":
                    self.listarprof_ordalf()
                case "8":
                    self.listartecadm_ordalf()
                case "9":
                    self.adicionar_veiculo()
                case "10":
                    print("Saindo do sistema...")
                    break
                case _:
                    print("Opção inválida. Tente novamente.")



    
    def adicionar_servidor(self):
        nome = input("digite o nome completo:")
        cpf = input("digite o cpf(11 digitos):")

        if any(s.cpf == novo_servidor.cpf for s in self.servidores):
            print(f"Servidor com CPF {cpf} não pode ser adicionado, pois já consta no sistema.")
            return
        
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


    def alterar_servidor(self):
        cpf = input("digite o cpf do servidor:")
        servidor: Servidor | None = None
        for s in self.servidores:
            if s.cpf == cpf:
                servidor = s
                break

        if not servidor:
            print(f"Servidor com CPF {cpf} não encontrado no sistema.")
            return
        
        
        print("Deixe em branco os espaços que não deseja alterar.")
        nome = input(f"Nome atual ({servidor.nome}): ") or servidor.nome
        SIAPE = input(f"SIAPE atual ({servidor.SIAPE}): ") or servidor.SIAPE
        rg = input(f"RG atual ({servidor.rg}): ") or servidor.rg
        endereço = input(f"Endereço atual ({servidor.endereço}): ") or servidor.endereço
        salário = input(f"Salário atual ({servidor.salário}): ") or servidor.salário
        dtnasc = input(f"Data de nascimento atual ({servidor.dtnasc}): ") or servidor.dtnasc
        tipo = input(f"Tipo atual ({servidor.tipo}): ") or servidor.tipo

        servidor.nome = nome
        servidor.SIAPE = SIAPE
        servidor.rg = rg
        servidor.endereço = endereço
        servidor.salário = salário
        servidor.dtnasc = dtnasc
        servidor.tipo = tipo
        print(f"Dados do servidor {servidor.nome} alterados no sistema.")


    def excluir_servidor(self, servidor: Servidor):
        if servidor in self.servidores:
            self.servidores.remove(servidor)
            print(f"Servidor {servidor.nome} removido do sistema.")
        else:
            print("Servidor não encontrado.")


    def dadoserv_cod(self, servidor: Servidor):
        cpf = int(input("Digite o cpf do servidor: "))
        servidor = None
        for s in self.servidores:
            if s.cpf == cpf:
                servidor = s
                break

        if servidor:
            print(f"\nDados do servidor {servidor.nome}:")
            print(f"Código: {servidor.codigo}")
            print(f"Nome: {servidor.nome}")
            print(f"SIAPE: {servidor.SIAPE}")
            print(f"RG: {servidor.rg}")
            print(f"CPF: {servidor.cpf}")
            print(f"Endereço: {servidor.endereço}")
            print(f"Salário: {servidor.salário}")
            print(f"Data de nascimento: {servidor.dtnasc}")
            print(f"Tipo: {servidor.tipo}")

        if servidor.veiculos:
                print("\nVeículos associados:")
                for veiculo in servidor.veiculos:
                    print(f" - {veiculo.marca} {veiculo.modelo} (Placa: {veiculo.placa})")
        else:
            print(f"Servidor com cpf {cpf} não encontrado.")

    

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


    def adicionar_veiculo(self):
        cpf = input("CPF do servidor: ")
        
        servidor = None
        for s in self.servidores:
            if s.cpf == cpf:
                servidor = s
                break

        if not servidor:
            print(f"Servidor com cpf {cpf} não encontrado no sistema.")
            return

        marca = input("Digite a marca do veículo: ")
        modelo = input("Digite o modelo do veículo: ")
        descricao = input("Digite a descrição do veículo: ")
        placa = input("Digite a placa do veículo: ")

        novo_veiculo = Veiculo(
            codigo=len(servidor.veiculos) + 1,
            descricao=descricao,
            placa=placa,
            marca=marca,
            modelo=modelo
        )
        servidor.veiculos.append(novo_veiculo)
        print(f"Veículo {marca} {modelo} adicionado com sucesso ao servidor {servidor.nome}.")

    def alterar_veiculo(self):
        codigo_veiculo = int(input("Digite o código do veículo: "))
        veiculo_encontrado = None
        servidor_dono = None

        for servidor in self.servidores:
            for veiculo in servidor.veiculos:
                if veiculo.codigo == codigo_veiculo:
                    veiculo_encontrado = veiculo
                    servidor_dono = servidor
                    break
            if veiculo_encontrado:
                break

        if veiculo_encontrado:
            print(f"Veículo encontrado no servidor {servidor_dono.nome}.")
            nova_marca = input(f"Marca atual ({veiculo_encontrado.marca}): ") or veiculo_encontrado.marca
            novo_modelo = input(f"Modelo atual ({veiculo_encontrado.modelo}): ") or veiculo_encontrado.modelo
            nova_descricao = input(f"Descrição atual ({veiculo_encontrado.descricao}): ") or veiculo_encontrado.descricao
            nova_placa = input(f"Placa atual ({veiculo_encontrado.placa}): ") or veiculo_encontrado.placa

            veiculo_encontrado.marca = nova_marca
            veiculo_encontrado.modelo = novo_modelo
            veiculo_encontrado.descricao = nova_descricao
            veiculo_encontrado.placa = nova_placa

            print(f"Veículo com código {codigo_veiculo} alterado com sucesso.")
        else:
            print(f"Veículo com código {codigo_veiculo} não encontrado.")

    def excluir_veiculo(self):
        codigo_veiculo = int(input("Digite o código do veículo a ser excluído: "))
        
        for servidor in self.servidores:
            for veiculo in servidor.veiculos:
                if veiculo.codigo == codigo_veiculo:
                    servidor.veiculos.remove(veiculo)
                    print(f"Veículo {veiculo.marca} {veiculo.modelo} removido do servidor {servidor.nome}.")
                    return
        
        print(f"Veículo com código {codigo_veiculo} não encontrado no sistema.")

    def dados_veiculo_codigo(self):
        codigo = int(input("Digite o código do veículo: "))
        
        for servidor in self.servidores:
            for veiculo in servidor.veiculos:
                if veiculo.codigo == codigo:
                    print("\nDados do veículo:")
                    print(f"Código: {veiculo.codigo}")
                    print(f"Marca: {veiculo.marca}")
                    print(f"Modelo: {veiculo.modelo}")
                    print(f"Descrição: {veiculo.descricao}")
                    print(f"Placa: {veiculo.placa}")
                    print(f"Proprietário: {servidor.nome} (Código: {servidor.codigo})")
                    return
        
        print(f"Veículo com código {codigo} não encontrado.")

    def listar_veiculos_servidor(self):
        cpf = input("CPF do servidor: ")
        
        servidor = None
        for s in self.servidores:
            if s.cpf == cpf:
                servidor = s
                break
        
        if not servidor:
            print(f"Servidor com cpf {cpf} não encontrado.")
            return
        
        if not servidor.veiculos:
            print(f"O servidor {servidor.nome} não possui veículos cadastrados.")
            return
        
        print(f"\nVeículos do servidor {servidor.nome}:")
        for veiculo in servidor.veiculos:
            print(f" - {veiculo.marca} {veiculo.modelo} (Placa: {veiculo.placa}, Código: {veiculo.codigo})")

    def listar_veiculos_servidor_ordem_alfabetica(self):
        cpf = input("CPF do servidor: ")
        servidor = None
        for s in self.servidores:
            if s.cpf == cpf:
                servidor = s
                break
        
        if not servidor:
            print(f"Servidor com cpf {cpf} não encontrado.")
            return
        
        if not servidor.veiculos:
            print(f"O servidor {servidor.nome} não possui veículos cadastrados.")
            return
        
        veiculos_ordenados = sorted(servidor.veiculos, key=lambda v: v.marca)
        
        print(f"\nVeículos do servidor {servidor.nome} (ordenados por marca):")
        for veiculo in veiculos_ordenados:
            print(f" - {veiculo.marca} {veiculo.modelo} (Placa: {veiculo.placa}, Código: {veiculo.codigo})")



sistema = Sistema()
sistema.menu_principal()