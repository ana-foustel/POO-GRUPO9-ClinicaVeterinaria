from clinica import Clinica
from cachorro import Cachorro
from gato import Gato

clinica = Clinica()

while True:
    print("\n1 - Cadastrar cachorro")
    print("2 - Cadastrar gato")
    print("3 - Listar animais")
    print("4 - Executar sons")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        raca = input("Raça: ")

        cachorro = Cachorro(nome, idade, raca)
