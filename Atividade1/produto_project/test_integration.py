import unittest
from unittest.mock import patch
from categoria import Categoria
from desktop import Desktop
from notebook import Notebook
from decorators_pt import DecoratorDesconto, DecoratorGarantia, ObservadorPreco
from gui import App
from tkinter import Tk

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.app = App(self.root)
        self.cat = Categoria(1, "Eletrônicos")

    def tearDown(self):
        self.root.destroy()

    @patch('tkinter.messagebox.showinfo')
    def test_desktop_registration_with_decorators(self, mock_showinfo):
        desktop = Desktop("Dell XPS", "Preto", 3000.0, self.cat, "500W")
        desktop_com_desconto = DecoratorDesconto(desktop, 10)
        desktop_com_garantia = DecoratorGarantia(desktop_com_desconto, 24)

        # Adicionar observador de preço
        observador = ObservadorPreco()
        desktop.anexar(observador)

        # Simulate registration in GUI with decorated product
        desktop_com_garantia.cadastrar()
        info = desktop_com_garantia.getInformacoes()

        # Alterar preço para disparar notificação
        desktop.preco = 2800.0

        self.assertIn("Dell XPS", info)
        self.assertIn("Desconto: 10%", info)
        self.assertIn("Garantia: 24 meses", info)

    @patch('tkinter.messagebox.showinfo')
    def test_notebook_registration_with_decorators(self, mock_showinfo):
        notebook = Notebook("MacBook Pro", "Cinza", 8000.0, self.cat, "10h")
        notebook_com_garantia = DecoratorGarantia(notebook, 12)
        notebook_com_desconto = DecoratorDesconto(notebook_com_garantia, 5)

        # Adicionar observador de preço
        observador = ObservadorPreco()
        notebook.anexar(observador)

        # Simulate registration in GUI with decorated product
        notebook_com_desconto.cadastrar()
        info = notebook_com_desconto.getInformacoes()

        # Alterar preço para disparar notificação
        notebook.preco = 7500.0

        self.assertIn("MacBook Pro", info)
        self.assertIn("Desconto: 5%", info)
        self.assertIn("Garantia: 12 meses", info)

if __name__ == '__main__':
    unittest.main()
