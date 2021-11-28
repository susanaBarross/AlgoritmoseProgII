from No import No

class Pilha:

    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def inserir(self, novo_elemento):
        no = No(novo_elemento)
        no.anterior = self.topo
        self.topo = no
        self.tamanho += 1

    def remover(self):
        if self.tamanho == 0:
            print("A pilha está vazia. Não há elemento para se remover!!!")
        else:
            self.topo = self.topo.anterior
            self.tamanho -= 1

    def __repr__(self):
        return str(self.topo) + '   ---   Tamanho da Pilha: ' + str(self.tamanho)
