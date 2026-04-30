def aprovar_emp(idade, emprestimo, renda_mensal):

    if idade >= 18 and emprestimo <= (renda_mensal * 20):
        return True
    return False


def calcular_total(parcelas, emprestimo, juros):
    parcela_mensal = emprestimo * (juros * ((1 + juros) ** parcelas) / ((1 + juros) ** parcelas) - 1)
    return parcela_mensal * parcelas


def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10


nome = input("Digite o nome da pessoa: ")

idade = int(input("Digite a idade: "))
while idade < 0 or idade > 115:
    print(f"Idade {idade} inválida! Tente entre 0 e 115.")
    idade = int(input("Digite a idade novamente: "))

renda_mensal = float(input("Digite a renda mensal: "))
while renda_mensal <= 0:
    print("A renda deve ser maior que zero.")
    renda_mensal = float(input("Digite a renda novamente: "))

emprestimo = float(input("Digite o valor do empréstimo: "))
while emprestimo <= 0:
    print("O valor do empréstimo deve ser maior que zero.")
    emprestimo = float(input("Digite o valor novamente: "))