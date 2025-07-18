'''
funcao saque:
apenas por nome (Keyword)
args: saldo, valor, extrato, limite, numero_saques, limite_saques
retorno: saldo, extrato

funcao deposito:
apenas por posicao
args: saldo, valor, extrato
retorno: saldo, extrato

funcao extrato:
deve receber por posicao e nome
args: saldo, args nomeados, extrato

criar usuario:
armazenar em lista
nome, data de nascimento, cpf(numeros), endereco(logadouro, numero, bairro, cidade/UF)
nao pode ter 2 usuarios com o mesmo cpf

criar conta conrrente:
armazenar em lista
agencia, numero da conta e usuario
numero da conta é sequencial, iniciando em 1
numero da agencia é fixo "0001" 
usuario pode ter mais de uma conta, mas uma conta pertence a somente um usuario


para vincular um usuario numa conta, filtra a lista de usuarios buscando o numero do cpf informado para cada usuario da lista
'''
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Digite o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Digite o valor do saque: ")) 
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "q":
            break

        else:
            print("Opcao Inválida!")

def menu():
    menu_texto = """
    ========== MENU ==========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Criar Usuário
    [nc] Criar Conta
    [q] Sair
    ==========================
    => """
    return input(menu_texto).strip().lower()


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque realizado com sucesso, saldo atual: R$ {saldo}")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
    else:
        print("Operacao falhou! o valor informado é Inválido!")
    return saldo, extrato

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
        
def criar_usuario(usuarios):
    cpf = input("Digite o seu CPF (apenas numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Ja existe um usuario com esse cpf")
        return 
    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento (dd-mm-aaaa):")
    endereco = input("Digite seu endereco (logadouro - nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})
    print("Usuario cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuario nao encontrado, fluxo de criacao de contas encerrado!")

main()

