from nodoArvore import NodoArvore
from percursosEmArvoresBinarias import ArvoreBinaria

if __name__== '__main__':
    """
            '+'
           /   \
        '2'    '*'
              /   \
            '4'   '6'

        Infixa
        2 + (4 * 6)

        Notação Polonesa
        +2*46
    
    """

    # insersão de forma manual
    arvore = ArvoreBinaria()

    n1 = NodoArvore('2')
    n2 = NodoArvore('+')
    n3 = NodoArvore('4')
    n4 = NodoArvore('*')
    n5 = NodoArvore('6')


    n2.esquerda = n1
    n2.direita = n4
    n4.esquerda = n3
    n4.direita = n5


    arvore.raiz = n2
    
    arvore.in_ordem()
