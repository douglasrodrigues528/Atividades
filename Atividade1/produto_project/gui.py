import tkinter as tk
from tkinter import ttk, messagebox
from categoria import Categoria
from desktop import Desktop
from notebook import Notebook

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Produtos")

        self.categorias = [
            Categoria(1, "Eletrônicos"),
            Categoria(2, "Informática"),
            Categoria(3, "Outros")
        ]

        self.criar_widgets()

    def criar_widgets(self):
        # Seleção do tipo de produto
        self.tipo_label = ttk.Label(self.root, text="Tipo de Produto:")
        self.tipo_label.grid(row=0, column=0, sticky="w")
        self.tipo_var = tk.StringVar()
        self.tipo_combo = ttk.Combobox(self.root, textvariable=self.tipo_var, state="readonly")
        self.tipo_combo['values'] = ("Desktop", "Notebook")
        self.tipo_combo.grid(row=0, column=1)
        self.tipo_combo.bind("<<ComboboxSelected>>", self.atualizar_formulario)

        # Modelo
        self.modelo_label = ttk.Label(self.root, text="Modelo:")
        self.modelo_label.grid(row=1, column=0, sticky="w")
        self.modelo_entry = ttk.Entry(self.root)
        self.modelo_entry.grid(row=1, column=1)

        # Cor
        self.cor_label = ttk.Label(self.root, text="Cor:")
        self.cor_label.grid(row=2, column=0, sticky="w")
        self.cor_entry = ttk.Entry(self.root)
        self.cor_entry.grid(row=2, column=1)

        # Preço
        self.preco_label = ttk.Label(self.root, text="Preço:")
        self.preco_label.grid(row=3, column=0, sticky="w")
        self.preco_entry = ttk.Entry(self.root)
        self.preco_entry.grid(row=3, column=1)

        # Categoria
        self.categoria_label = ttk.Label(self.root, text="Categoria:")
        self.categoria_label.grid(row=4, column=0, sticky="w")
        self.categoria_var = tk.StringVar()
        self.categoria_combo = ttk.Combobox(self.root, textvariable=self.categoria_var, state="readonly")
        self.categoria_combo['values'] = [cat.nome for cat in self.categorias]
        self.categoria_combo.grid(row=4, column=1)

        # Rótulo e entrada para atributo específico (mudará com base no tipo de produto)
        self.specific_label = ttk.Label(self.root, text="")
        self.specific_label.grid(row=5, column=0, sticky="w")
        self.specific_entry = ttk.Entry(self.root)
        self.specific_entry.grid(row=5, column=1)

        # Botão de envio
        self.submit_button = ttk.Button(self.root, text="Cadastrar", command=self.cadastrar)
        self.submit_button.grid(row=6, column=0, columnspan=2, pady=10)

    def atualizar_formulario(self, event):
        tipo = self.tipo_var.get()
        if tipo == "Desktop":
            self.specific_label.config(text="Potência da Fonte:")
        elif tipo == "Notebook":
            self.specific_label.config(text="Tempo de Bateria:")
        else:
            self.specific_label.config(text="")
        self.specific_entry.delete(0, tk.END)

    def cadastrar(self):
        tipo = self.tipo_var.get()
        modelo = self.modelo_entry.get()
        cor = self.cor_entry.get()
        preco = self.preco_entry.get()
        categoria_nome = self.categoria_var.get()
        especifico = self.specific_entry.get()

        if not (tipo and modelo and cor and preco and categoria_nome and especifico):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        try:
            preco = float(preco)
        except ValueError:
            messagebox.showerror("Erro", "Preço deve ser um número.")
            return

        categoria = next((cat for cat in self.categorias if cat.nome == categoria_nome), None)
        if not categoria:
            messagebox.showerror("Erro", "Categoria inválida.")
            return

        if tipo == "Desktop":
            produto = Desktop(modelo, cor, preco, categoria, especifico)
        elif tipo == "Notebook":
            produto = Notebook(modelo, cor, preco, categoria, especifico)
        else:
            messagebox.showerror("Erro", "Tipo de produto inválido.")
            return

        produto.cadastrar()
        messagebox.showinfo("Sucesso", f"{tipo} cadastrado com sucesso!\n\n{produto.getInformacoes()}")
        self.limpar_formulario()

    def limpar_formulario(self):
        self.tipo_combo.set('')
        self.modelo_entry.delete(0, tk.END)
        self.cor_entry.delete(0, tk.END)
        self.preco_entry.delete(0, tk.END)
        self.categoria_combo.set('')
        self.specific_entry.delete(0, tk.END)
        self.specific_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
