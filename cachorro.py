from animal import Animal


class Cachorro(Animal):
    """Representa um cachorro."""

    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.__raca = raca

    def emitir_som(self):
        return "Au au!"

    def passear(self):
        return "O cachorro está passeando."