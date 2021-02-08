from Clases.Arbol import Arbol
from Clases.Nodo import Nodo


class Gestor:

    def __init__(self):
        self.arbol = Arbol()

    def agregar(self, dato):
        nodo = Nodo(dato)
        return self.arbol.insertarDatos(dato)

    def inorden(self):
        return self.arbol.inorder()

    def postorden(self):
        return self.arbol.postorder()

    def preorden(self):
        return self.arbol.preorder()
