def test(nota):
    while nota < 0 or nota > 10:
        print(f"A nota {nota} é inválida! Digite um valor entre 0 e 10.")
        nota = float(input("Digite a nota novamente: "))
    return nota

nota_cp1 = float(input("Digite a nota do 1º Checkpoint: "))
nota_cp1 = test(nota_cp1)
nota_cp2 = float(input("Digite a nota do 2º Checkpoint: "))
nota_cp2 = test(nota_cp2)
nota_cp3 = float(input("Digite a nota do 3º Checkpoint: "))
nota_cp3 = test(nota_cp3)
nota_sprint1 = float(input("Digite sua nota do 1º sprint: "))
nota_sprint1 = test(nota_sprint1)
nota_sprint2 = float(input("Digite sua nota do 2º sprint: "))
nota_sprint2 = test(nota_sprint2)
nota_globs = float(input("Digite sua nota do Global Solution: "))
nota_globs = test(nota_globs)

if nota_cp1 >= nota_cp2:
    menor = nota_cp2
else:
    menor = nota_cp1
if nota_cp3 < menor:
    menor = nota_cp3

media = (((nota_cp1 + nota_cp2 + nota_cp3 - menor + nota_sprint1 + nota_sprint2) / 4) * 0.4) + (nota_globs * 0.6)

media_cmpeso = media * 0.4
print()
print("===========================")
print("Calculo da media:")
print(f"((({nota_cp1:.1f} + {nota_cp2:.1f} + {nota_cp3:.1f} - {menor:.1f} + {nota_sprint1:.1f} + {nota_sprint2:.1f}) / 4) * 0.4) + ({nota_globs:.1f} * 0.6)")
print(f"Sua média do sementre: {media:.1f}")
print(f"Sua média com peso: {media_cmpeso:.1f}")
print("===========================")
