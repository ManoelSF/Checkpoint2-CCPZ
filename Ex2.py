# RM:569174 ALUNO:JOSUÉ FRANCO BRAGA

print("="*10,"CP2 - PCP", "="*10)

# Ao invés de inicializar 3 valores optei por uma lista e um for para preencher ele
valores = []
# Guarda o número a ser movido
aux = 0

for c in range (0, 3):
    num = float(input(f"Digite o {c}º valor: "))
    valores.append(num)

# O loop externo garante a verificação varias vezes
for i in range(len(valores)):
    # O loop interno faz a verificação e a troca de valores
    for j in range(0, len(valores) - 1):
        if valores[j] < valores[j + 1]:
            aux = valores[j]
            valores[j] = valores[j + 1]   
            valores[j + 1] = aux          
            
### CONDICIONAIS
# Condição de existência
if valores[0] >= valores[1] + valores[2]:
    print("Não forma um triângulo!")
else:
    if valores[0] == valores[1] == valores[2]:
        print("Triângulo Equilátero!", end="")
    elif valores[0] == valores[1] or valores[0] == valores[2] or valores[1] == valores[2]:
        print("Triângulo Isósceles!", end="")
    else:
        # Não foi pedido o escaleno mas é o mais condizente e lógico para o else nessa situação
        print("Triãngulo Escaleno! ", end="")
        

if valores[0]**2 == valores[1]**2 + valores[2]**2:
        print("O ângulo dele é classificado como Retângulo!")
elif valores[0]**2 > valores[1]**2 + valores[2]**2:
        print("O ângulo dele é classificado como Obtusâgulo!")
elif valores[0]**2 < valores[1]**2 + valores[2]**2:
        print("O ângulo dele é classificado como Acutângulo!")
