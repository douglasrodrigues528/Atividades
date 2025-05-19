from produto import Produto

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria  # strongly private attribute

    @property
    def tempoDeBateria(self):
        return self.__tempoDeBateria

    @tempoDeBateria.setter
    def tempoDeBateria(self, value):
        self.__tempoDeBateria = value

    def getInformacoes(self):
        base_info = super().getInformacoes()
        return f"{base_info}, Tempo de Bateria: {self.__tempoDeBateria}"

    def cadastrar(self):
        # Implementation of cadastrar for Notebook
        print(f"Notebook cadastrado: {self.getInformacoes()}")
