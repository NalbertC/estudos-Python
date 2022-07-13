from nodoArvore import NodoArvore

class ArvoreBinaria:
    def __init__(self, chave=None):
        if chave is None:
            nodo = NodoArvore(chave)
            self.raiz = nodo
        else:
            self.raiz = None
            
    def in_ordem(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        
        if nodo.esquerda:
            print('(', end='')
            self.in_ordem(nodo.esquerda)
        
        print(nodo, end=' ')
        if nodo.direita:
            self.in_ordem(nodo.direita)
            print(')', end='')

    def pre_ordem (self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        print(nodo, end=' ')
        if nodo.esquerda:
            self.pre_ordem(nodo.esquerda)
        if nodo.direita:
            self.pre_ordem(nodo.direita)

    def pos_ordem (self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo.esquerda:
            self.pos_ordem(nodo.esquerda)
        if nodo.direita:
            self.pos_ordem(nodo.direita)
        print(nodo, end=' ')