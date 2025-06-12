from produto import Produto

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potenciaDaFonte  # weakly private attribute

    @property
    def potenciaDaFonte(self):
        return self._potenciaDaFonte

    @potenciaDaFonte.setter
    def potenciaDaFonte(self, value):
        self._potenciaDaFonte = value

    def getInformacoes(self):
        base_info = super().getInformacoes()
        return f"{base_info}, Potência da Fonte: {self._potenciaDaFonte}"

    def cadastrar(self):
        # Implementation of cadastrar for Desktop
        print(f"Desktop cadastrado: {self.getInformacoes()}")
