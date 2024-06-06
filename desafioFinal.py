def menu():
    menu = """\n
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [cc] Criar Nova Conta
        [cu] Criar Novo Usuario
        [q] Sair
        => """
    return input(menu)

def depositar(saldo, extrato, valor, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado no valor de: R$", valor)
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def saque(*, saldo, limite, extrato, valor, numeroSaques, limiteSaques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numeroSaques >= limiteSaques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numeroSaques += 1
        print("Saque realizado no valor de: R$", valor)
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numeroSaques

def exibirExtrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criarUsuario(usuarios):
    cpf = input("Informe os números do CPF (sem pontos e traços): ")
    usuario = filtrarUsuarios(cpf, usuarios)

    if usuario:
        print("Este CPF já está em uso.")
        return
    
    nome = input("Informe seu nome: ")
    dataNascimento = input("Informe a data do seu nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (utilize 'nome da rua', 'número', 'bairro' e 'cidade/sigla do estado'):")

    usuarios.append({"nome": nome, "dataNascimento": dataNascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso")

def filtrarUsuarios(cpf, usuarios):
    usuariosFiltrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuariosFiltrados[0] if usuariosFiltrados else None

def criarConta(agencia, numeroConta, usuarios):
    cpf = input("Informe os números do CPF (sem pontos e traços): ")
    usuario = filtrarUsuarios(cpf, usuarios)
    if usuario:
        print("Sua conta foi criada com sucesso")
        print(f"Agência: {agencia}\nNúmero da Conta: {numeroConta}")
        return {"agencia": agencia, "numeroConta": numeroConta, "usuario": usuario}
    
    print("Este CPF não está vinculado a nenhum usuário cadastrado.")
    return None


def programa():
    agencia = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numeroSaques = 0
    limiteSaques = 3
    numeroConta = 1
    contas = []
    usuarios = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, extrato, valor)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numeroSaques = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numeroSaques=numeroSaques,
                limiteSaques=limiteSaques,
            )

        elif opcao == "e":
            exibirExtrato(saldo, extrato=extrato)

        elif opcao == "cc":
            conta = criarConta(agencia, numeroConta, usuarios)
            if conta:
                contas.append(conta)
                numeroConta += 1

        elif opcao == "cu":
            criarUsuario(usuarios)  

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

programa()