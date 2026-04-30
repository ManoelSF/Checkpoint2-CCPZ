print("Códigos de origem da carga")
print("     ----------------")
print("     |Estado|Imposto|")
print("     |   1  |  35%  |")
print("     |   2  |  25%  |")
print("     |   3  |  15%  |")
print("     |   4  |   5%  |")
print("     |   5  | isento|")
print("     ----------------")

num_caminhao = int(input("Digite o código de origem da carga do caminhão: "))

while True:
    if num_caminhao < 1:
        print("Número invalido")
        num_caminhao = int(input("Digite o código de origem da carga do caminhão: "))

    elif num_caminhao > 5:
        print("Número invalido")
        num_caminhao = int(input("Digite o código de origem da carga do caminhão: "))

    elif num_caminhao == 1:
        imposto = 35
        break

    elif num_caminhao == 2:
        imposto = 25
        break

    elif num_caminhao == 3:
        imposto = 15
        break

    elif num_caminhao == 4:
        imposto = 5
        break

    elif num_caminhao == 5:
        imposto = 0
        break

peso_caminhao = float(input("Digite o peso do caminhão(t): "))

while peso_caminhao <= 0:
    print("Peso invalido")
    peso_caminhao = float(input("Digite o peso do caminhão(t): "))

print("-----------------------------------")
print("|Códigos de carga|  Preço por kg  |")
print("|    10  a  20   |   R$: 100,00   |")
print("|    21  a  30   |   R$: 250,00   |")
print("|    31  a  40   |   R$: 340,00   |")
print("-----------------------------------")

cod_carga = int(input("Digite o código de carga do caminhão: "))

while True:
    if cod_carga < 10:
        print("Número invalido")
        cod_carga = int(input("Digite o código de carga do caminhão: "))

    elif cod_carga > 40:
        print("Número invalido")
        cod_carga = int(input("Digite o código de carga do caminhão: "))

    elif cod_carga >= 10 and cod_carga <= 20:
        preco_kilo = 100
        break

    elif cod_carga >= 21 and cod_carga <= 30:
        preco_kilo = 250
        break

    elif cod_carga >= 30:
        preco_kilo = 340
        break

peso_kilo = peso_caminhao * 1000
preco_carga = preco_kilo * peso_kilo
imposto_pago = (imposto / 100) * preco_carga
valor_total = preco_carga + imposto_pago

print()
print(f"Peso em toneladas: {peso_caminhao:.2f}t")

print(f"Peso em kilo: {peso_kilo}kg")

print(f"Código de origem: {num_caminhao} e imposto: {imposto}%")

print(f"Código de carga: {cod_carga} e preço por kg: R$ {preco_kilo:.2f}")

print(f"O preço da carga é: {peso_kilo:.2f}kg * {preco_kilo:.2f} = {preco_carga:.2f}")

print(f"O valor total é: {preco_carga:.2f}kg + {imposto_pago:.2f} = {valor_total:.2f}")



