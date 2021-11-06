from No import No

class ListaDuplaEncadeada:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    
    def adicionar(self, dado):

        # Cria um novo no apontando para None (anterior e proximo)
        no = No(dado, None, None)

        # Se o inicio for None a lista esta vazia
        # O inicio e o fim recebem o novo no
        if self.inicio is None:
            self.inicio = no
            self.fim = no

        # Caso ja exista algum valor na lista
        else:
            # O anterior aponta para o fim
            no.anterior = self.fim
            # O proximo aponta para None
            no.proximo = None
            # O proximo do fim sempre aponta para o novo no
            self.fim.proximo = no
            # O fim passa a ser o novo no
            self.fim = no


    def imprimir(self):
        
        print("Lista duplamente encadeada na ordem dos elementos adicionados: ")

        # O no atual e o primeiro no da lista
        no_atual = self.inicio

        no = ""
        # Para cada no valido da lista
        while no_atual is not None:
            if no_atual.anterior is None:
                no += "None "
            no += "<---> | " + str(no_atual.dado) + " | "
            if no_atual.proximo is None:
                no += "<---> None"

            no_atual = no_atual.proximo
        print(no)
        print("=" * 110)



    def imprimir_invertido(self): 

        
        print("Lista duplamente encadeada em ordem invertida: ")

        # O no atual e o ultimo no da lista
        no_atual = self.fim

        no = ""
        # Para cada no valido da lista
        while no_atual is not None:
            if no_atual.proximo is None:
                no += "None "
            no += "<---> | " + str(no_atual.dado) + " | "
            if no_atual.anterior is None:
                no += "<---> None"

            no_atual = no_atual.anterior
        print(no)
        print("=" * 110)
