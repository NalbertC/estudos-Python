class  NodoArvore:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

    def __str__(self):
        return str(self.chave)