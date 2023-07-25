import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [0]\tSair
    => """


    return input(textwrap.dedent(menu))

def deposit(balance: float, val: float, extract: list):
    if val < 0:
        print("Você só pode depositar quantias positivas.\n")
    
    else:
        balance+= val
        extract.append(val)
        print("\nDepósito realizado com sucesso!\n")

    return balance, extract

'''def withdraw(balance: float, val: float, extract: list, withdraws: int):
    if val > balance or val > 500:
        print("\nNão é possível sacar essa quantia, ou você não possui saldo suficiente ou o valor excede o limite para saque.\n")

    elif withdraws >= 3:
        print("\nVocê atingiu o limite de saques diários.\n")

    else:
        total -= val
        extract.append(-val)
        withdraws += 1
        print("\nSaque realizado com sucesso!\n")

    return balance, extract, withdraws'''

def withdraw(balance: float, val: float, extract: list, limite: float, numero_saques: int, limite_saques: int):
    if val > balance or val > limite:
        print("\nNão é possível sacar essa quantia, ou você não possui saldo suficiente ou o valor excede o limite para saque.\n")

    elif numero_saques >= limite_saques:
        print("\nVocê atingiu o limite de saques diários.\n")

    else:
        balance -= val
        extract.append(-val)
        numero_saques += 1
        print("\nSaque realizado com sucesso!\n")

    return balance, extract, numero_saques



def showExtract(extract: list):
    for val in extract:
        if val > 0:
            print("R$%.2f depositados\n" %val)
        else:
            print("R$%.2f sacados\n" %val)

def searchUser(cpf: int, users: list):
    userSearched = [user for user in users if user["cpf"] == cpf]
    if userSearched:
        return userSearched[0]
    
    else:
        return None

def userRegister(userList: list):
    cpf = int(input("Insira seu CPF sem pontuação: \n"))
    if searchUser(cpf, userList):
        print("O CPF inserido já está cadastrado no sistema.\n")
    
    else:
        name = input("Insira seu nome completo: \n")
        adress = input("Insira seu endereço no seguinte formato: logradouro, número, bairro, cidade/sigla do estado\n")
        birthDate = input("Insira sua data de nascimento no seguinte formato: DD/MM/AA\n")
        userList.append({"cpf":cpf, "name":name, "adress":adress, "birthDate":birthDate})
        print("\nUsuário criado com sucesso!\n")

        return userList

def createAccount(agency: str, accountNumber: int, users: list):
    cpf = int(input("Informe o CPF do usuário: "))
    user = searchUser(cpf, users)

    if user:
        print("\n=== Conta criada com sucesso! ===")
        return {"agency": agency, "accountNumber": accountNumber, "user": user}

    print("\n-Usuário não encontrado, fluxo de criação de conta encerrado")

def listAccounts(accounts: list):
    for account in accounts:
        line = f"""\
            Agência:\t{account['agency']}
            C/C:\t\t{account['accountNumber']}
            Titular:\t{account['user']['name']}
        """
        print("=" * 100)
        print(textwrap.dedent(line))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = deposit(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = withdraw(
                saldo=saldo,
                val=valor,
                extract=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            showExtract(extrato)

        elif opcao == "6":
            userRegister(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = createAccount(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listAccounts(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()

