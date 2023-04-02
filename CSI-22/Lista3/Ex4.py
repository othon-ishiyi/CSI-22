class ape_resenha:
    apartamento = '203B'
    def __init__(self, nome):
        self.nome = nome
    def morador(self):
        print(self.nome)
    @classmethod
    def mudar_de_ape(cls, novo_ape):
        ape_resenha.apartamento = novo_ape
    @staticmethod
    def frase_de_efeito():
        print('Acabou a família')

#static method não precisa de objeto
ape_resenha.frase_de_efeito()

A = ape_resenha('Linguini')
B = ape_resenha('Profeta')
C = ape_resenha('Catia')
D = ape_resenha('Arroz')

#class method independe do objeto
ape_resenha.mudar_de_ape('203E')
print(D.apartamento)

#metodo de instancia acessa o objeto
D.morador()

    