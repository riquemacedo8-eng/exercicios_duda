#atividade funções
#Q1

def maior_numero(numeros: list): 
  maior = numeros[0]
  for numero in numeros[1:]:
    if numero > maior:
       maior = numero
 
lista = [1, 3, 5, 10]
maior = maior_numero(lista)
print(maior)

#Q2

def contador_vogais(palavra: str) -> int:
    qtd_vogal = 0
    for letra in palavra:
        if letra in "aeiou":
            qtd_vogal +=1
    return qtd_vogal
    
nome = "henrique"
total = contador_vogais(nome)
print(total)

#Q3

def calcular_media(numeros:list[int]) -> float:
   return sum(numeros)/len(numeros)

#Q4

def calcular_potencia(base: int, expoente: int) -> int:
   return base ** expoente

resultado = calcular_potencia(5,2)
print(resultado)


