from categoria import Categoria
from desktop import Desktop
from notebook import Notebook
from decorators_pt import DecoratorDesconto, DecoratorGarantia

def test_decorators():
    cat = Categoria(1, "Eletrônicos")

    desktop = Desktop("Dell XPS", "Preto", 3000.0, cat, "500W")
    notebook = Notebook("MacBook Pro", "Cinza", 8000.0, cat, "10h")

    # Aplicar decoradores
    desktop_com_desconto = DecoratorDesconto(desktop, 10)  # 10% de desconto
    desktop_com_garantia = DecoratorGarantia(desktop_com_desconto, 24)  # 24 meses de garantia

    notebook_com_garantia = DecoratorGarantia(notebook, 12)  # 12 meses de garantia
    notebook_com_desconto = DecoratorDesconto(notebook_com_garantia, 5)  # 5% de desconto

    # Imprimir informações
    print("Desktop com desconto e garantia:")
    print(desktop_com_garantia.getInformacoes())
    desktop_com_garantia.cadastrar()

    print("\\nNotebook com garantia e desconto:")
    print(notebook_com_desconto.getInformacoes())
    notebook_com_desconto.cadastrar()

if __name__ == "__main__":
    test_decorators()
