from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def atualizar(self, sujeito):
        pass

class Sujeito(ABC):
    def __init__(self):
        self._observadores = []

    def anexar(self, observador: Observador):
        if observador not in self._observadores:
            self._observadores.append(observador)

    def desanexar(self, observador: Observador):
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar(self):
        for observador in self._observadores:
            observador.atualizar(self)

class EstrategiaPreco(ABC):
    @abstractmethod
    def calcular_preco(self, preco):
        pass

class Produto(Sujeito, ABC):
    def __init__(self, modelo, cor, preco, categoria, estrategia_preco: EstrategiaPreco = None):
        super().__init__()
        self.modelo = modelo
        self.cor = cor
        self._preco = preco
        self.categoria = categoria
        self._estrategia_preco = estrategia_preco

    @property
    def preco(self):
        if self._estrategia_preco:
            return self._estrategia_preco.calcular_preco(self._preco)
        return self._preco

    @preco.setter
    def preco(self, valor):
        self._preco = valor
        self.notificar()

    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: {self.preco}, Categoria: {self.categoria}"

    @abstractmethod
    def cadastrar(self):
        pass
