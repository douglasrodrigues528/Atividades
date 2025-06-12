from produto import Produto

class DecoratorProduto(Produto):
    def __init__(self, produto):
        self._produto = produto

    def getInformacoes(self):
        return self._produto.getInformacoes()

    def cadastrar(self):
        self._produto.cadastrar()

class DecoratorDesconto(DecoratorProduto):
    def __init__(self, produto, percentual_desconto):
        super().__init__(produto)
        self._percentual_desconto = percentual_desconto

    def getInformacoes(self):
        info_base = self._produto.getInformacoes()
        valor_desconto = self._produto.preco * (self._percentual_desconto / 100)
        preco_com_desconto = self._produto.preco - valor_desconto
        return f"{info_base}, Desconto: {self._percentual_desconto}%, Preço com Desconto: {preco_com_desconto:.2f}"

class DecoratorGarantia(DecoratorProduto):
    def __init__(self, produto, meses_garantia):
        super().__init__(produto)
        self._meses_garantia = meses_garantia

    def getInformacoes(self):
        info_base = self._produto.getInformacoes()
        return f"{info_base}, Garantia: {self._meses_garantia} meses"
