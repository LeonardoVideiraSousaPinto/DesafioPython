# arquivo: arvore.py

# Definição da classe Nodo, que representa um nó da árvore
class Nodo:
    def __init__(self, valor):
        """
        Inicializa um nó com um valor e filhos esquerdo e direito como None.
        :param valor: O valor armazenado no nó.
        """
        self.valor = valor
        self.esquerdo = None
        self.direito = None

# Definição da classe ArvoreBinaria, que representa a árvore binária
class ArvoreBinaria:
    def __init__(self):
        """
        Inicializa a árvore com a raiz como None.
        """
        self.raiz = None

    def inserir(self, valor):
        """
        Insere um novo valor na árvore.
        :param valor: O valor a ser inserido.
        """
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, nodo, valor):
        """
        Método auxiliar para inserção recursiva de valores.
        :param nodo: O nó atual onde a inserção deve ser feita.
        :param valor: O valor a ser inserido.
        """
        if valor < nodo.valor:
            if nodo.esquerdo is None:
                nodo.esquerdo = Nodo(valor)
            else:
                self._inserir_recursivo(nodo.esquerdo, valor)
        else:
            if nodo.direito is None:
                nodo.direito = Nodo(valor)
            else:
                self._inserir_recursivo(nodo.direito, valor)

    def travessia_em_ordem(self):
        """
        Realiza a travessia em ordem da árvore.
        :return: Uma lista com os valores dos nós visitados na travessia em ordem.
        """
        return self._travessia_em_ordem_recursivo(self.raiz, [])

    def _travessia_em_ordem_recursivo(self, nodo, travessia):
        """
        Método auxiliar para travessia recursiva em ordem.
        :param nodo: O nó atual.
        :param travessia: A lista que acumula os valores dos nós.
        :return: A lista de valores em travessia em ordem.
        """
        if nodo:
            self._travessia_em_ordem_recursivo(nodo.esquerdo, travessia)
            travessia.append(nodo.valor)
            self._travessia_em_ordem_recursivo(nodo.direito, travessia)
        return travessia

if __name__ == '__main__':
    import unittest

    class TesteArvoreBinaria(unittest.TestCase):
        def setUp(self):
            """
            Configura um novo objeto ArvoreBinaria para cada teste.
            """
            self.arvore = ArvoreBinaria()

        def test_inserir_e_travessia_em_ordem(self):
            """
            Testa a inserção de múltiplos valores e a travessia em ordem.
            """
            # Inserir elementos na árvore
            self.arvore.inserir(10)
            self.arvore.inserir(5)
            self.arvore.inserir(15)
            self.arvore.inserir(3)
            self.arvore.inserir(7)
            self.arvore.inserir(12)
            self.arvore.inserir(17)

            # Testar a travessia em ordem
            self.assertEqual(self.arvore.travessia_em_ordem(), [3, 5, 7, 10, 12, 15, 17])

        def test_inserir_nodo_unico(self):
            """
            Testa a inserção de um único elemento.
            """
            # Inserir um único elemento
            self.arvore.inserir(5)

            # Testar a travessia em ordem
            self.assertEqual(self.arvore.travessia_em_ordem(), [5])

        def test_inserir_valores_duplicados(self):
            """
            Testa a inserção de valores duplicados.
            """
            # Inserir valores duplicados
            self.arvore.inserir(10)
            self.arvore.inserir(10)
            self.arvore.inserir(5)
            self.arvore.inserir(5)

            # Testar a travessia em ordem
            self.assertEqual(self.arvore.travessia_em_ordem(), [5, 5, 10, 10])

    unittest.main()
