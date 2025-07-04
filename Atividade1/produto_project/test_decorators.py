from categoria import Categoria
from desktop import Desktop
from notebook import Notebook
from decorators_pt import DecoratorDesconto, DecoratorGarantia, EstrategiaDesconto, ObservadorPreco

def test_decorators():
    cat = Categoria(1, "Eletrônicos")

    desktop = Desktop("Dell XPS", "Preto", 3000.0, cat, "500W")
    notebook = Notebook("MacBook Pro", "Cinza", 8000.0, cat, "10h")

    # Aplicar decoradores
    desktop_com_desconto = DecoratorDesconto(desktop, 10)  # 10% de desconto
    desktop_com_garantia = DecoratorGarantia(desktop_com_desconto, 24)  # 24 meses de garantia

    notebook_com_garantia = DecoratorGarantia(notebook, 12)  # 12 meses de garantia
    notebook_com_desconto = DecoratorDesconto(notebook_com_garantia, 5)  # 5% de desconto

    # Testar Strategy diretamente
    estrategia = EstrategiaDesconto(20)
    preco_original = 100
    preco_com_desconto = estrategia.calcular_preco(preco_original)
    assert preco_com_desconto == 80, "Erro na estratégia de desconto"

    # Testar Observer
    observador = ObservadorPreco()
    desktop.anexar(observador)
    desktop.preco = 2500.0  # Deve disparar notificação

    # Imprimir informações
    print("Desktop com desconto e garantia:")
    print(desktop_com_garantia.getInformacoes())
    desktop_com_garantia.cadastrar()

    print("\\nNotebook com garantia e desconto:")
    print(notebook_com_desconto.getInformacoes())
    notebook_com_desconto.cadastrar()

if __name__ == "__main__":
    test_decorators()
