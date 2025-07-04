from produto import Produto, EstrategiaPreco, Observador

class DecoratorProduto(Produto):
    def __init__(self, produto):
        self._produto = produto

    def __getattr__(self, name):
        return getattr(self._produto, name)

    def getInformacoes(self):
        return self._produto.getInformacoes()

    def cadastrar(self):
        self._produto.cadastrar()

class EstrategiaDesconto(EstrategiaPreco):
    def __init__(self, percentual_desconto):
        self._percentual_desconto = percentual_desconto

    def calcular_preco(self, preco):
        desconto = preco * (self._percentual_desconto / 100)
        return preco - desconto

class DecoratorDesconto(DecoratorProduto):
    def __init__(self, produto, percentual_desconto):
        super().__init__(produto)
        self._estrategia_desconto = EstrategiaDesconto(percentual_desconto)
        self._percentual_desconto = percentual_desconto

    def getInformacoes(self):
        info_base = self._produto.getInformacoes()
        preco_com_desconto = self._estrategia_desconto.calcular_preco(self._produto.preco)
        return f"{info_base}, Desconto: {self._percentual_desconto}%, Preço com Desconto: {preco_com_desconto:.2f}"

class DecoratorGarantia(DecoratorProduto):
    def __init__(self, produto, meses_garantia):
        super().__init__(produto)
        self._meses_garantia = meses_garantia

    def getInformacoes(self):
        info_base = self._produto.getInformacoes()
        return f"{info_base}, Garantia: {self._meses_garantia} meses"

class ObservadorPreco(Observador):
    def atualizar(self, sujeito):
        print(f"Alerta: O preço do produto '{sujeito.modelo}' foi alterado para {sujeito.preco}")
