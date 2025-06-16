'''
Criar um sistema bancario com as operaçõess: Sacar, depositar e visualizar extrato
Operação de deposito: Depositar valores positivos para a conta bancaria,  
todos os depositos devem ser armazenados em uma variavel e exibidos na operação de extrato

Operação de saque: deve permitir 3 saques diarios, com limite maximo de 500 reais por saque,
caso nao tenha saldo em conta, deve exibir uma mensagem informando que nao sera possivel por falta de saldo,
todos os saques devem ser armazenados em uma variavel e exibidos na operação de extrato

Operação de extrato: deve listar todos os depositos e saques realizados na conta, no fim, deve exibir o saldo atual da conta
devem ser exibidos utilizando o formato R$ xxx.xx
'''
menu = '''
Bem vindo ao menu do banco
Selecione a operação desejada:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
->
'''
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        print("Opção selecionada: Deposito")
        print(f"Seu saldo atual é R$ {saldo:.2f}")
        valor_deposito = float(input("Digite o valor que voce deseja depositar: "))
        if valor_deposito <= 0:
            print("Digite um valor maior que 0 reais para depositar!")
        else:
            saldo += valor_deposito
            extrato += f"deposito: R$ {valor_deposito:.2f}\n"
        print(f"Seu saldo agora é R$ {saldo:.2f}")


    elif opcao == "s":
        print("Opção selecionada: Saque")
        print(f"Seu saldo atual é R$ {saldo:.2f}")
        valor_saque = float(input("Digite o valor que voce deseja sacar: "))
        if (valor_saque <= saldo) and (valor_saque <= limite) and (valor_saque > 0):
            if LIMITE_SAQUES == 0:
                print("Voce ja utilizou o maximo de vezes essa opção hoje, tente novamente amanha.")
                print(f"Seu saldo atual é R$ {saldo}")
            else:            
                saldo -= valor_saque
                LIMITE_SAQUES -= 1
                numero_saques += 1
                extrato += f"saque: R$ {valor_saque:.2f}\n"
                print(f"Seu saldo agora é R$ {saldo:.2f}, voce ainda pode sacar {LIMITE_SAQUES} hoje")
        else:
            print("Nao foi possivel realizar o saque pois o a quantia que deseja sacar é maior do que o saldo atual ou limite")
        # ainda falta armazenar no extrato
    elif opcao == "e":
        print("Opção selecionada: Extrato")
        print(extrato)
        print(f"Seu saldo atual é de R$ {saldo:.2f}")
    elif opcao == "q":
        break
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")