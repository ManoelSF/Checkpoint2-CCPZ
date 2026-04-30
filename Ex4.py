nome = input("Digite o nome do funcionario: ")

print("Códigos de cargos")
print("---------------------")
print("|Código|    Cargo   |")
print("|   1  |   Gerente  |")
print("|   2  |  Analista  |")
print("|   3  | Assistente |")
print("|   4  | Estagiário |")
print("---------------------")

cod = int(input("Digite o código do cargo: "))
while cod < 0 or cod > 4:
    print(f"O código {cod} é inválido! Digite um valor entre 1 e 4.")
    cod = int(input("Digite o código do cargo novamente: "))

if cod == 1:
    cargo = 'Gerente'
elif cod == 2:
    cargo = 'Analista'
elif cod == 3:
    cargo = 'Assistente'
elif cod == 4:
    cargo = 'Estagiário'

salario_base = float(input("Digite o salário base do funcionario: "))

while salario_base < 0:
    print("O valor não pode ser negativo!")
    salario_base = float(input("Digite o salario base do funcionario novamente: "))

horas_extras = float(input("Digite o total de horas extras trabalhadas do funcionario: "))

while horas_extras < 0:
    print("O valor não pode ser negativo!")
    horas_extras = float(input("Digite o total de horas extras trabalhadas do funcionario novamente: "))

faltas = int(input("Digite o total de faltas(dias) do mês: "))
while faltas < 0:
    print("O valor não pode ser negativo!")
    faltas = int(input("Digite o total de faltas(dias) do mês novamente: "))

print("Bônus por cargos")
print("----------------------")
print("| Bônus |    Cargo   |")
print("|R$ 1000|   Gerente  |")
print("|R$ 500 |  Analista  |")
print("|R$ 300 | Assistente |")
print("|R$ 100 | Estagiário |")
print("----------------------")
print()
bonus = input("O funcionário vai receber bônus por desempenho? (S/N): ")

while bonus not in 'SsNn':
    print("Resposta inválida.")
    bonus = input("O funcionário vai receber bônus por desempenho? (S/N): ")

def parabenizar(nome):
    print(f"Parabéns {nome} pelo seu desempenho!")

def calcular_hr_ex(salario_base, horas_extras):
    horas_extras = horas_extras * (1.5/100) * salario_base
    return horas_extras

def calcular_desconto_falta(salario_base, faltas):
    faltas = faltas * (2/100) * salario_base
    return faltas

def calcular_bonus(cod, bonus):
    if bonus in 'Ss':
        bonus_aplicavel = "Sim"
        if cod == 1:
            bonus = 1000
        elif cod == 2:
            bonus = 500
        elif cod == 3:
            bonus = 300
        elif cod == 4:
            bonus = 100
    else:
        bonus_aplicavel = "Não"
        bonus = 0
    return bonus, bonus_aplicavel



total_hr_ex = calcular_hr_ex(salario_base, horas_extras)

desconto_falta = calcular_desconto_falta(salario_base, faltas)

bonus, bonus_aplicavel = calcular_bonus(cod, bonus)

salario = salario_base  + bonus + total_hr_ex - desconto_falta

print(f"O salário bruto de {nome}: R$ {salario_base:.2f}")
print(f"Acréssimos:")
print(f"Bônus foi aplicado?: {bonus_aplicavel}")
if bonus != 0:
    print(f"Bônus: R$ {bonus:.2f}")
print(f"Horas extras trabalhadas: {horas_extras} h")
print(f"Valor das horas trabalhadas: R$ {total_hr_ex}")
print(f"Descontos: ")
print(f"Desconto de falta: R$ {desconto_falta:.2f}")
print(f"Salário final: R$ {salario:.2f}")






