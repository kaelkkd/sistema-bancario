MAX_WITHDRAWS =  3
MAX_DEP_VAL = 500
extract = []
total = 0
withdraws = 0

while True:

    x = int(input("Escolha a operação desejada:\nSaque [1] \nDepósito [2] \nVerificar extrato [3]\n"))

    if x == 1:
        val = float(input("Insira a quantidade que desejar sacar:\n"))
        if val > total:
            print("\nNão é possível sacar um valor acima do que há em sua conta.\n")
        elif withdraws >= MAX_WITHDRAWS:
            print("\nVocê atingiu o limite máximo de saques diários\n")
        elif val > 500:
            print("\nVocê não pode sacar mais de R$500.\n")
        else:
            total -= val
            extract.append(-val)
            withdraws += 1
            print("\nSaque realizado com sucesso!\n")

    elif x == 2:
        dep = float(input("Insira a quantidade que deseja depositar:\n"))
        total += dep
        extract.append(dep)
        print("\nDepósito realizado com sucesso!\n")

    elif x == 3:
        for n in extract:
            if n > 0:
                print("R$%.2f depositados\n" %n)
            else:
                print("R$%.2f sacados\n" %n)

    else:
        break