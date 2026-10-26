import aulas.algoritimos.menu as menu

while True:
    menu.exibir()
    opcao = input("Digite uma opção: ")

    if opcao == "1":
        cadastro = menu.aluno()
    elif opcao == "2":
        cadastro = menu.professor()
    elif opcao == "0":
        break
    else:
        print("Opção inválida")

print("Até breve... fim do programa!")




