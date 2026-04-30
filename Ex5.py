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

print("\nTaxa de Juros")
print("---------------------")
print("|Parcelas|   Juros  |")
print("| 3 - 6  | 5% ao mês|")
print("| 7 - 12 | 8% ao mês|")
print("| 13 - 24|10% ao mês|")
print("---------------------")

parcelas = int(input("Digite o número de parcelas (3-24): "))
while parcelas < 3 or parcelas > 24:
    print(f"Valor {parcelas} inválido!")
    parcelas = int(input("Digite o número de parcelas entre 3 e 24: "))


if aprovar_emp(idade, emprestimo, renda_mensal):
    juros = definir_taxa(parcelas)
    total_pagar = calcular_total(parcelas, emprestimo, juros)

    print(f"\n✅ Empréstimo APROVADO para {nome}!")
    print(f"Taxa aplicada: {juros * 100:.0f}% ao mês")
    print(f"Valor total com juros: R$ {total_pagar:.2f}")
    print(f"Valor de cada parcela ({parcelas}x): R$ {total_pagar / parcelas:.2f}")
else:
    print(f"\n Empréstimo NEGADO para {nome}.")
    if idade < 18:
        print("Motivo: Menor de idade.")
    else:
        print("Motivo: Valor solicitado excede o limite de 20x a renda mensal.")
