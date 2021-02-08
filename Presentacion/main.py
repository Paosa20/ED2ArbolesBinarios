from Gestor.Gestor import Gestor


def instrucciones():
    gestor = Gestor()

    print(gestor.agregar(4))
    print(gestor.agregar(5))
    print(gestor.agregar(6))
    print(gestor.agregar(2))
    print("Se muestra el inorden: ")
    print(gestor.inorden())
    print("Se muestra el postorden: ")
    print(gestor.postorden())
    print("Se muestra el preorden")
    print(gestor.preorden())


if __name__ == '__main__':
    instrucciones()
