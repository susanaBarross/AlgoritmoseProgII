class No:
    def __init__(self, dado=0, no_anterior=None):
        self.dado = dado
        self.anterior = no_anterior

    def __repr__(self):
        return '%s\n%s' % (self.dado, self.anterior)
