menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Valor depositado com sucesso!")
            
        else: 
             print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITES_SAQUES

        if excedeu_saldo:      
            print("Operação falhou! O valor solicitado ultrapassou o saldo disponível.")
        elif excedeu_limite:
            print("Operação falhou! O valor ultrapassou o limite.")
        elif excedeu_saque:
            print("Operação falhou! Você ultrapassou o número de saques.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido") 
    
    elif opcao == "e":
        print("\n=====================Extrato=========================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("======================================================")
    elif opcao == "q":
        break  
    else:
        print("Operação inválida, por favor selecione a operação desejada.")

