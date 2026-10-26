def exibir():
    print("+--------------------------------------+")
    print("| 1. Para Inserir um aluno            |")
    print("| 2. Para Inserir um Professor        |")
    print("| 0. Sair                              |")
    print("+--------------------------------------+")
    print()


def aluno():
    ra = input("Digite o RA: ")
    nome = input("Digite o nome completo: ")
    return {"ra": ra, "nome": nome}


def professor():
    ra = input("Digite o RA: ")
    nome = input("Digite o nome completo: ")
    curso = input("Digite o nome do curso: ")
    return {"ra": ra, "nome": nome, "curso": curso}

