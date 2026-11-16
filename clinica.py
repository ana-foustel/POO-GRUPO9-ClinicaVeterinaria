class Clinica:
    """Gerencia os animais da clínica."""

    def __init__(self):
        self.__animais = []

    def cadastrar_animal(self, animal):
        self.__animais.append(animal)

    def listar_animais(self):
        for animal in self.__animais:
            print(animal).