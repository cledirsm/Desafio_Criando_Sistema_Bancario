# Operação de depósito

# Deve ser possível depositar valores positivos para minha conta bancária.
# A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos
# nos preocupar em identificar qual é o número da agência e conta bancária.
# Todos os depósitos devem ser armazenados em uma variável e exibidos na operação 
# de extrato.

# Operação de saque

# O Sistema deve permitir realizar 3 saques diários com limite de R$500,00 por saque.
# Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando
# que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser 
# armazenados em uma variável e exibidos na operação de extrato.

# Operação de extrato

# Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da
# da listagem deve ser exibido o saldo atual da conta. Os valores devem ser exibidos utilizando
# o formato R$ xxx.xx Ex 1500.45 = R$ 1500.45

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
n_saques = 0
limite_saques = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: {valor:.2f}\n"
            
        else:
            print("Operação falhou! Ovalor informado é inválido!")
        
    elif opcao == "2":
        valor = float(input("Informe o valor de saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = n_saques >= limite_saques
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
            
        elif excedeu_saques:
            print("Operação falhou! Número de saques diáarios excedido.")
            
        elif valor >0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            n_saques += 1
        
    elif opcao == "3":
        print("\n********** EXTRATO **********")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("********************")
        
    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada!")