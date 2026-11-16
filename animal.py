from animal import Animal


class Gato(Animal):
    """Representa um gato."""

    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self.__cor = cor

    def emitir_som(self):
        return "Miau!"