'''
def saudacao(nome):
    print("Ola", nome)

saudacao("Hhenrique")
'''
'''
def contagem():
    for i in range(10, 20):
        print(i * 2)
contagem()
'''
'''
def verificar():

    while True:
        numero =  int(input("digite uma idade:"))
        if numero > 18:
            print("Maior de idade")
        
        elif numero < 18:
            print("Menor de idade")
verificar()
'''

def mostrar_nomes():
    nomes = ["Ana", "João", "Carlos"]
    
    for nome in nomes:
        print(nome)

mostrar_nomes()