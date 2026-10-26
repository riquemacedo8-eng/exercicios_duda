#Questao 7 lista 4.2

def eTerra(ilha: list[list[int]], i: int, j: int) -> bool:
    if i >= 0 and i< len(ilha) and j >= 0:
        return ilha[i][j] != 0 
    return False

def criarIlhas(matriz: list[str], oceano:list[list[int]]) -> list[list[int]]:
    for i in range(len(matriz)):
        linha = matriz[i]
        for j in range(len(linha)):
            letra = linha [j]
        for letra in linha:
            oceano[i][j] = 4 if letra.upper() == 'X' else 0

def criarOceano(tam: int) -> list[list[int]]:
    oceano = []
    for i in range(tam):
        oceano.append([])
        for j in range(tam):
            oceano[i].append(0)
    return oceano

def balancearIlhas(oceano:list[list[int]]):
    for i in range(len(oceano)):
        for j in range(len(oceano[i])):
            if eTerra(oceano, i, j):
                aCima = 1 if eTerra(oceano, i, j -1) else 0 
            embaixo = 1 if eTerra(oceano, i, j +1) else 0 
            direita = 1 if eTerra(oceano, i + 1, j ) else 0
            esquerda = 1 if eTerra(oceano, i - 1, j ) else 0
            oceano [i][j] -= (aCima + embaixo + direita + esquerda)

def perimetro(oceano:list[list[int]]) -> int:
    soma = 0
    for linha in oceano:
        soma += sum(linha)

def exibir(matriz:list[list[int]]):
    print("---------------------------------")
    for linha in matriz:
        print(linha)
    print("-------------------------------")





'''
lista = ['XOO','XOX','OOX']
oceano = criarOceano(3)
print(oceano)
criarIlhas(lista, oceano)
print("==========================")
print(oceano)
'''