'''
def calcular_desconto(valor: float, desconto: float) -> float:
    valor_descontado = valor * desconto / 100
    resultado = valor - valor_descontado
    return resultado 
'''
'''
def ordenar_lista(lista: list [int]) -> list[int]:
    print(f" atual: {lista}")
    for j in range(1, len(lista)):
        for i in range(len(lista) - j):
            atual =  lista[i]
            proximo = lista [i+1]

            if atual > proximo:
                lista[i] = proximo
                lista[i+1] = atual
                
    print(f"Ordenado: {lista}")        
    return lista

lista = [2, 5, 1, 9, 8, 3]
resolucao = ordenar_lista(lista)
print(resolucao) 
'''

