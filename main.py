from classes import Animal, Cachorro, Gato

animais = []


def cadastrar():
    print("\n===== CADASTRO DE ANIMAL =====")

    print("1 - Cachorro")
    print("2 - Gato")

    tipo = input("Escolha o tipo de animal: ")

    nome = input("Nome do animal: ")
    idade = int(input("Idade do animal: "))
    tutor = input("Nome do tutor: ")
    raca = input("Raça do animal: ")

    if tipo == "1":
        animal = Cachorro(nome, idade, tutor, raca)

    elif tipo == "2":
        animal = Gato(nome, idade, tutor, raca)

    else:
        print("Tipo inválido!")
        return

    animais.append(animal)

    print("\nAnimal cadastrado com sucesso!")


def listar():
    print("\n===== ANIMAIS CADASTRADOS =====")

    if not animais:
        print("Nenhum animal cadastrado.")
        return

    for i, animal in enumerate(animais, start=1):
        print(f"\nPaciente {i}")
        print(animal)


def buscar():
    print("\n===== BUSCAR PACIENTE =====")

    nome = input("Digite o nome do animal: ")

    encontrado = False

    for animal in animais:
        if animal.nome.lower() == nome.lower():
            print("\nPaciente encontrado!")
            print(animal)
            encontrado = True

    if not encontrado:
        print("Paciente não encontrado.")


def executar_acao_polimorfica():
    print("\n===== ATENDIMENTO VETERINÁRIO =====")

    if not animais:
        print("Nenhum paciente cadastrado.")
        return

    for animal in animais:
        print(f"\nAtendimento de: {animal.nome}")
        animal.atender()


def menu():
    while True:

        print("\n================================")
        print("     CLÍNICA VETERINÁRIA")
        print("================================")
        print("1 - Cadastrar paciente")
        print("2 - Listar pacientes")
        print("3 - Buscar paciente")
        print("4 - Realizar atendimento")
        print("5 - Sair")
        print("================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()

        elif opcao == "2":
            listar()

        elif opcao == "3":
            buscar()

        elif opcao == "4":
            executar_acao_polimorfica()

        elif opcao == "5":
            print("\nObrigado por utilizar nosso sistema!")
            print("Encerrando...")
            break

        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()