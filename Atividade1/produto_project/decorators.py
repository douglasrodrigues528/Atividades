from produto import Produto

class ProdutoDecorator(Produto):
    def __init__(self, produto):
        self._produto = produto

    def getInformacoes(self):
        return self._produto.getInformacoes()

    def cadastrar(self):
        self._produto.cadastrar()

class DiscountDecorator(ProdutoDecorator):
    def __init__(self, produto, discount_percent):
        super().__init__(produto)
        self._discount_percent = discount_percent

    def getInformacoes(self):
        base_info = self._produto.getInformacoes()
        discount_amount = self._produto.preco * (self._discount_percent / 100)
        discounted_price = self._produto.preco - discount_amount
        return f"{base_info}, Desconto: {self._discount_percent}%, Preço com Desconto: {discounted_price:.2f}"

class WarrantyDecorator(ProdutoDecorator):
    def __init__(self, produto, warranty_months):
        super().__init__(produto)
        self._warranty_months = warranty_months

    def getInformacoes(self):
        base_info = self._produto.getInformacoes()
        return f"{base_info}, Garantia: {self._warranty_months} meses"
