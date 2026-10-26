def decrescente(lista: list[int]):
    for j in range(len(lista)):
        for i in range(len(lista) -1):
            atual = lista[i]
            proximo = lista[i + 1]

            if atual < proximo:
                lista[i], lista[i + 1] = proximo, atual

    return lista

xpto = [3, 5, 4, 2, 1]

resultado = decrescente(xpto)



print(f"Resultado: {resultado}")