Sistema de Cadastro de Produtos com Interface Gráfica
Este projeto é uma aplicação em Python que permite o cadastro de produtos de informática, 
especificamente Desktops e Notebooks, com uma interface gráfica amigável feita com tkinter.
O sistema é orientado a objetos e modularizado, facilitando a manutenção e expansão.

Estrutura do Projeto
produto.py
Contém a definição da classe abstrata Produto, que representa os atributos e comportamentos comuns a todos os produtos:
Atributos: modelo, cor, preço, categoria
Método abstrato: cadastrar(), que deve ser implementado pelas subclasses

desktop.py
Define a classe Desktop, que herda de Produto e adiciona o atributo:
potenciaDaFonte: potência da fonte do computador
Implementa o método cadastrar(), que realiza o cadastro do desktop.

notebook.py
Define a classe Notebook, que herda de Produto e adiciona o atributo:
tempoDeBateria: duração da bateria do notebook em horas
Implementa o método cadastrar().

categoria.py
Define a classe Categoria, que representa a categoria do produto com os seguintes atributos:
id: identificador da categoria
nome: nome da categoria

gui.py
Implementa a interface gráfica do sistema utilizando tkinter:
Permite ao usuário escolher o tipo de produto (Desktop ou Notebook)
Os campos do formulário são dinamicamente adaptados conforme o tipo selecionado
Realiza a validação dos campos e chama o método cadastrar() correspondente


Padrões Criacionais Utilizados:

Padrão Factory Method (Método de Fábrica) Implícito:
O projeto utiliza o conceito do Factory Method ao criar instâncias das subclasses Desktop ou Notebook dinamicamente na interface gráfica (gui.py), com base na escolha do usuário.
A classe abstrata Produto funciona como o produto base, e as subclasses Desktop e Notebook são as implementações concretas.
A criação do objeto correto é feita no método cadastrar da classe App (gui.py), que decide qual classe instanciar conforme o tipo selecionado.
Por que foi escolhido:

Para garantir que todos os produtos compartilhem uma interface comum (definida pela classe abstrata Produto), facilitando a manutenção e extensão do código.
Para permitir a criação flexível de diferentes tipos de produtos sem modificar o código cliente (a interface gráfica).
Para promover o princípio aberto/fechado, permitindo adicionar novos tipos de produtos facilmente.
Como foi implementado:

No arquivo produto.py, a classe abstrata Produto define a interface comum:

from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self, modelo, cor, preco, categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: {self.preco}, Categoria: {self.categoria}"

    @abstractmethod
    def cadastrar(self):
        pass
No arquivo gui.py, a criação dos objetos Desktop ou Notebook ocorre dinamicamente:

  if tipo == "Desktop":
      produto = Desktop(modelo, cor, preco, categoria, especifico)
  elif tipo == "Notebook":
      produto = Notebook(modelo, cor, preco, categoria, especifico)
  else:
      messagebox.showerror("Erro", "Tipo de produto inválido.")
      return

O código cliente (a interface gráfica) não precisa conhecer os detalhes da criação dos objetos, apenas utiliza a interface comum Produto.
Este é um exemplo simples e eficaz do uso do padrão Factory Method para criação de objetos em um sistema orientado a objetos.
