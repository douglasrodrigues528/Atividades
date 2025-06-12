import unittest
from unittest.mock import patch
from tkinter import Tk
from gui import App

class TestGUI(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.app = App(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('tkinter.messagebox.showerror')
    def test_empty_fields(self, mock_showerror):
        self.app.tipo_combo.set('')
        self.app.modelo_entry.delete(0, 'end')
        self.app.cor_entry.delete(0, 'end')
        self.app.preco_entry.delete(0, 'end')
        self.app.categoria_combo.set('')
        self.app.specific_entry.delete(0, 'end')

        self.app.cadastrar()
        mock_showerror.assert_called_with("Erro", "Por favor, preencha todos os campos.")

    @patch('tkinter.messagebox.showerror')
    def test_invalid_price(self, mock_showerror):
        self.app.tipo_combo.set('Desktop')
        self.app.modelo_entry.insert(0, 'Dell XPS')
        self.app.cor_entry.insert(0, 'Preto')
        self.app.preco_entry.insert(0, 'abc')
        self.app.categoria_combo.set('Eletrônicos')
        self.app.specific_entry.insert(0, '500W')

        self.app.cadastrar()
        mock_showerror.assert_called_with("Erro", "Preço deve ser um número.")

    @patch('tkinter.messagebox.showerror')
    def test_invalid_category(self, mock_showerror):
        self.app.tipo_combo.set('Desktop')
        self.app.modelo_entry.insert(0, 'Dell XPS')
        self.app.cor_entry.insert(0, 'Preto')
        self.app.preco_entry.insert(0, '3000')
        self.app.categoria_combo.set('Categoria Inválida')
        self.app.specific_entry.insert(0, '500W')

        self.app.cadastrar()
        mock_showerror.assert_called_with("Erro", "Categoria inválida.")

    @patch('tkinter.messagebox.showinfo')
    def test_successful_desktop_registration(self, mock_showinfo):
        self.app.tipo_combo.set('Desktop')
        self.app.modelo_entry.insert(0, 'Dell XPS')
        self.app.cor_entry.insert(0, 'Preto')
        self.app.preco_entry.insert(0, '3000')
        self.app.categoria_combo.set('Eletrônicos')
        self.app.specific_entry.insert(0, '500W')

        self.app.cadastrar()
        mock_showinfo.assert_called()
        args = mock_showinfo.call_args[0]
        self.assertIn('Dell XPS', args[1])
        self.assertIn('500W', args[1])

    @patch('tkinter.messagebox.showinfo')
    def test_successful_notebook_registration(self, mock_showinfo):
        self.app.tipo_combo.set('Notebook')
        self.app.modelo_entry.insert(0, 'MacBook Pro')
        self.app.cor_entry.insert(0, 'Cinza')
        self.app.preco_entry.insert(0, '8000')
        self.app.categoria_combo.set('Eletrônicos')
        self.app.specific_entry.insert(0, '10h')

        self.app.cadastrar()
        mock_showinfo.assert_called()
        args = mock_showinfo.call_args[0]
        self.assertIn('MacBook Pro', args[1])
        self.assertIn('10h', args[1])

if __name__ == '__main__':
    unittest.main()
