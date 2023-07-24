MAX_WITHDRAWS =  3
MAX_DEP_VAL = 500
AGENCY = "0001"
extract = []
total = 0
withdraws = 0

def deposit(balance: float, val: float, extract: list):
    if val < 0:
        print("Você só pode depositar quantias positivas.\n")
    
    else:
        balance+= val
        extract.append(val)

    return balance, extract

def withdraw(balance: float, val: float, extract: list, withdraws: int):
    if val > balance or val > 500:
        print("\nNão é possível sacar essa quantia, ou você não possui saldo suficiente ou o valor excede o limite para saque.\n")

    elif withdraws > MAX_WITHDRAWS:
        print("\nVocê atingiu o limite de saques diários.\n")

    else:
        total -= val
        extract.append(-val)
        withdraws += 1
        print("\nSaque realizado com sucesso!\n")

    return balance, extract, withdraws

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
        userList.appen({"cpf":cpf, "name":name, "adress":adress, "birthDate":birthDate})

        return userList

def createAccount()


