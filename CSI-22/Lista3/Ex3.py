from abc import ABC, abstractmethod

class Bebida(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def info(self):
        pass

class Suco(Bebida):
    def __init__(self, tamanho, sabor):
        self.tamanho = tamanho
        self.sabor = sabor
    def info(self):
        print("Oi, eu sou o suco de {0}, o seu amigão!".format(self.sabor))

class Refri(Bebida):
    def __init__(self, tamanho, sabor):
        self.tamanho = tamanho
        self.sabor = sabor
    def info(self):
        print("Oi, eu sou o refri de {0}, o seu amigola!".format(self.sabor))

class Café(Bebida):
    def __init__(self, tamanho):
        self.tamanho = tamanho
    def info(self):
        print("Oi, eu sou o cafezinho, o seu amiguinho!")

café = Café(200)
limonada = Suco(500, 'limão')
coca = Refri(1000, 'cola')

for i in [café, limonada, coca]:
    i.info()

    