class ListaContigua:
    def __init__(self, max_size=10):
        self.lista = []
        self.max_size = max_size

    def insertar(self, valor):
        if len(self.lista) < self.max_size:
            self.lista.append(valor)
        else:
            print("Lista llena.")

    def eliminar(self, valor):
        if valor in self.lista:
            self.lista.remove(valor)
        else:
            print("Valor no encontrado.")

    def mostrar(self):
        print("Lista Contigua:", self.lista)


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaLigada:
    def __init__(self, max_size=10):
        self.cabeza = None
        self.size = 0
        self.max_size = max_size

    def insertar(self, valor):
        if self.size < self.max_size:
            nuevo_nodo = Nodo(valor)
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            self.size += 1
        else:
            print("Lista llena.")

    def eliminar(self, valor):
        actual = self.cabeza
        previo = None
        while actual and actual.valor != valor:
            previo = actual
            actual = actual.siguiente
        if actual:
            if previo:
                previo.siguiente = actual.siguiente
            else:
                self.cabeza = actual.siguiente
            self.size -= 1
        else:
            print("Valor no encontrado.")

    def mostrar(self):
        actual = self.cabeza
        print("Lista Ligada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("NULL")


class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDoblementeLigada:
    def __init__(self, max_size=10):
        self.cabeza = None
        self.size = 0
        self.max_size = max_size

    def insertar(self, valor):
        if self.size < self.max_size:
            nuevo_nodo = NodoDoble(valor)
            if self.cabeza:
                self.cabeza.anterior = nuevo_nodo
                nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            self.size += 1
        else:
            print("Lista llena.")

    def eliminar(self, valor):
        actual = self.cabeza
        while actual and actual.valor != valor:
            actual = actual.siguiente
        if actual:
            if actual.anterior:
                actual.anterior.siguiente = actual.siguiente
            if actual.siguiente:
                actual.siguiente.anterior = actual.anterior
            if actual == self.cabeza:
                self.cabeza = actual.siguiente
            self.size -= 1
        else:
            print("Valor no encontrado.")

    def mostrar(self):
        actual = self.cabeza
        print("Lista Doblemente Ligada:", end=" ")
        while actual:
            print(actual.valor, end=" <-> ")
            actual = actual.siguiente
        print("NULL")


class ListaIndexada:
    def __init__(self, max_size=10):
        self.lista = []
        self.indices = []
        self.max_size = max_size

    def insertar(self, valor):
        if len(self.lista) < self.max_size:
            self.lista.append(valor)
            self.indices.append(len(self.lista))
        else:
            print("Lista llena.")

    def eliminar(self, valor):
        if valor in self.lista:
            idx = self.lista.index(valor)
            self.lista.pop(idx)
            self.indices.pop(idx)
        else:
            print("Valor no encontrado.")

    def mostrar(self):
        print("Lista Indexada:")
        for i in range(len(self.lista)):
            print(f"Índice: {self.indices[i]} -> Valor: {self.lista[i]}")


def menu_secundario(lista):
    while True:
        print("\nSeleccione una opción:")
        print("1. Insertar dato")
        print("2. Eliminar dato")
        print("3. Mostrar lista")
        print("4. Volver al menú principal")
        opcion = input("Ingrese opción: ")
        
        if opcion == "1":
            valor = input("Ingrese valor: ")
            lista.insertar(valor)
        elif opcion == "2":
            valor = input("Ingrese valor a eliminar: ")
            lista.eliminar(valor)
        elif opcion == "3":
            lista.mostrar()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")


def menu_principal():
    while True:
        print("\nSeleccione el tipo de lista a probar:")
        print("1. Lista Contigua (Arreglo)")
        print("2. Lista Ligada (Simple)")
        print("3. Lista Doblemente Ligada")
        print("4. Lista Indexada")
        print("5. Salir")
        opcion = input("Ingrese opción: ")
        
        if opcion == "1":
            menu_secundario(ListaContigua())
        elif opcion == "2":
            menu_secundario(ListaLigada())
        elif opcion == "3":
            menu_secundario(ListaDoblementeLigada())
        elif opcion == "4":
            menu_secundario(ListaIndexada())
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()