from Clases.Nodo import Nodo


class Arbol(object):

    def __init__(self):
        self.raiz = None

    def insert(self, raiz, dato):

        if raiz is None:
            raiz = Nodo(dato)
        else:
            d = raiz.dato
            if dato < d:
                raiz.left = self.insert(raiz.left, dato)
            else:
                raiz.right = self.insert(raiz.right, dato)
        return raiz.dato

    def insertarDatos(self, dato):

        return self.insert(self.raiz, dato)

    def inorder(self):
        return self.inordenRecursivo(self.raiz)

    def inordenRecursivo(self, raiz):

        if raiz is None:
            return None
        else:
            return self.inordenRecursivo(raiz.left), self.inordenRecursivo(raiz.right)

    def preorder(self):
        return self.preordenRecursivo(self.raiz)

    def preordenRecursivo(self, raiz):

        if raiz is None:
            return None
        else:
            return self.preordenRecursivo(raiz.left), self.preordenRecursivo(raiz.right)

    def postorder(self):
        return self.postordenRecursivo(self.raiz)

    def postordenRecursivo(self, raiz):

        if raiz is None:
            return None
        else:
            return self.postordenRecursivo(raiz.left), self.postordenRecursivo(raiz.right)
