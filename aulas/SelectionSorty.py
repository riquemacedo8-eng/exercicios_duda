def selectionsorty(lista):
    tam = len(lista)
    for i in range(tam):
        menor = lista[i]
        indice = i 
        for j in range(i+1, tam):
            if lista[j] < menor:
                indice, menor = j, lista [j]

        lista[i], lista[indice] = menor, lista[i]

    return lista