#Q2 LAÇOS
'''
binario = input("Digite um binário: ")

decimal = int(binario, 2)

print(decimal)
'''

'''
#q3
frase = input("Digite uma frase: ")

palavras = frase.split()

for palavra in palavras:
    if len(palavra) >= 5:
        print("#" + palavra.capitalize(), end=" ")
        '''

''' Q1
segundos = int(input("digite os segundos:"))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
seg = segundos % 60

if horas > 0:
    print(f"{horas} hora, {minutos} minuto e {seg} segundos")

elif minutos > 0:
    print(f"{minutos} minuto e {seg} segundos")

else:
    print(f"{seg} segundos")
    '''

matriz = []

print("Digite os números da matriz 3x3:")

for i in range(3):
    linha = []

    for j in range(3):
        numero = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(numero)

    matriz.append(linha)

soma = matriz[0][0] + matriz[1][1] + matriz[2][2]

print("A soma da diagonal principal é:", soma)
