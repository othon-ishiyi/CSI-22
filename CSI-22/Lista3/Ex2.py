class Inimigo:
    def gritar(self):
        raise NotImplementedError
    
class Tartaruga:
    def __init__(self, vida):
        self.vida = vida

class Koopa(Tartaruga, Inimigo):
    def __init__(self, vida):
        super().__init__(vida)
    def gritar(self):
        print("hahaha tenho ainda {0} vidas!".format(self.vida))


koopa = Koopa(2)
print(koopa.vida)
koopa.gritar()
print(koopa.__class__.mro())