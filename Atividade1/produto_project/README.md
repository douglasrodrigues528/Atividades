# Atualização final da documentação


## Sistema de Cadastro de Produtos com Interface Gráfica

Este projeto é uma aplicação em Python que permite o cadastro de produtos de informática, especificamente Desktops e Notebooks, com uma interface gráfica amigável feita com tkinter. O sistema é orientado a objetos e modularizado, facilitando a manutenção e expansão.

### Estrutura do Projeto

- **produto.py**  
  Contém a definição da classe abstrata Produto, que representa os atributos e comportamentos comuns a todos os produtos:  
  - Atributos: modelo, cor, preço, categoria  
  - Método abstrato: cadastrar(), que deve ser implementado pelas subclasses

- **desktop.py**  
  Define a classe Desktop, que herda de Produto e adiciona o atributo:  
  - potenciaDaFonte: potência da fonte do computador  
  Implementa o método cadastrar(), que realiza o cadastro do desktop.

- **notebook.py**  
  Define a classe Notebook, que herda de Produto e adiciona o atributo:  
  - tempoDeBateria: duração da bateria do notebook em horas  
  Implementa o método cadastrar().

- **categoria.py**  
  Define a classe Categoria, que representa a categoria do produto com os seguintes atributos:  
  - id: identificador da categoria  
  - nome: nome da categoria

- **gui.py**  
  Implementa a interface gráfica do sistema utilizando tkinter:  
  - Permite ao usuário escolher o tipo de produto (Desktop ou Notebook)  
  - Os campos do formulário são dinamicamente adaptados conforme o tipo selecionado  
  - Realiza a validação dos campos e chama o método cadastrar() correspondente

---

## Padrões Criacionais Utilizados

### Padrão Factory Method (Método de Fábrica) Implícito

O projeto utiliza o conceito do Factory Method ao criar instâncias das subclasses Desktop ou Notebook dinamicamente na interface gráfica (gui.py), com base na escolha do usuário. A classe abstrata Produto funciona como o produto base, e as subclasses Desktop e Notebook são as implementações concretas. A criação do objeto correto é feita no método cadastrar da classe App (gui.py), que decide qual classe instanciar conforme o tipo selecionado.

**Por que foi escolhido:**

- Para garantir que todos os produtos compartilhem uma interface comum (definida pela classe abstrata Produto), facilitando a manutenção e extensão do código.  
- Para permitir a criação flexível de diferentes tipos de produtos sem modificar o código cliente (a interface gráfica).  
- Para promover o princípio aberto/fechado, permitindo adicionar novos tipos de produtos facilmente.

**Como foi implementado:**

No arquivo produto.py, a classe abstrata Produto define a interface comum:

```python
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
```

No arquivo gui.py, a criação dos objetos Desktop ou Notebook ocorre dinamicamente:

```python
if tipo == "Desktop":
    produto = Desktop(modelo, cor, preco, categoria, especifico)
elif tipo == "Notebook":
    produto = Notebook(modelo, cor, preco, categoria, especifico)
else:
    messagebox.showerror("Erro", "Tipo de produto inválido.")
    return
```

O código cliente (a interface gráfica) não precisa conhecer os detalhes da criação dos objetos, apenas utiliza a interface comum Produto. Este é um exemplo simples e eficaz do uso do padrão Factory Method para criação de objetos em um sistema orientado a objetos.

---

## Documentação Atualizada do Projeto parte 2 - Padrões Estruturais e Melhorias

### Visão Geral

Este projeto implementa um sistema de cadastro de produtos com foco em reutilização, flexibilidade e extensibilidade, utilizando padrões estruturais de design para melhorar a arquitetura e facilitar futuras manutenções e expansões.

### Padrões Estruturais Implementados

- **Decorator:**  
  Utilizado para adicionar funcionalidades adicionais aos produtos sem modificar suas classes originais. As classes DecoratorDesconto e DecoratorGarantia permitem aplicar descontos e garantias aos produtos dinamicamente.

**Exemplo de aplicação no código:**

```python
from decorators_pt import DecoratorDesconto, DecoratorGarantia
from desktop import Desktop
from categoria import Categoria

cat = Categoria(1, "Eletrônicos")
desktop = Desktop("Dell XPS", "Preto", 3000.0, cat, "500W")

# Aplicando decoradores
desktop_com_desconto = DecoratorDesconto(desktop, 10)  # 10% de desconto
desktop_com_garantia = DecoratorGarantia(desktop_com_desconto, 24)  # 24 meses de garantia

print(desktop_com_garantia.getInformacoes())
desktop_com_garantia.cadastrar()
```

### Testes Abrangentes

Foram criados testes unitários para os decoradores, garantindo a correta aplicação de descontos e garantias. Testes para a interface gráfica (GUI) foram implementados, cobrindo validação de campos, tratamento de erros e cadastro bem-sucedido para produtos Desktop e Notebook. Testes de integração foram adicionados para verificar a interação entre decoradores e o fluxo de cadastro.

### Interface Gráfica (GUI)

Desenvolvida com Tkinter, a GUI permite o cadastro de produtos Desktop e Notebook, com campos específicos para cada tipo. A interface valida entradas, exibe mensagens de erro e confirmações, e limpa o formulário após o cadastro.

**Exemplo de uso na GUI:**

- Seleção do tipo de produto e preenchimento dos campos na interface gráfica  
  `self.tipo_combo['values'] = ("Desktop", "Notebook")`

- Campos específicos para Desktop: Potência da Fonte  
- Campos específicos para Notebook: Tempo de Bateria

### Melhorias Realizadas

- Implementação de testes unitários e de integração para garantir a robustez do sistema.  
- Estruturação do código para suportar facilmente a adição de novos padrões estruturais e funcionalidades.

---

## Trabalho Padrões: Terceira fase - Padrões Comportamentais

### Visão Geral

Nesta fase, o projeto foi aprimorado com a implementação de padrões comportamentais para aumentar a flexibilidade e reutilização dos comportamentos dos produtos.

### Padrões Comportamentais Implementados

- **Strategy:**  
  Implementado para permitir estratégias flexíveis de cálculo de preço. A classe abstrata `EstrategiaPreco` define a interface para estratégias de preço, e a classe `EstrategiaDesconto` implementa uma estratégia concreta de desconto percentual. O padrão Strategy foi integrado à classe `Produto`, permitindo que o preço seja calculado dinamicamente conforme a estratégia aplicada.

- **Observer:**  
  Implementado para notificar observadores sobre mudanças no estado do produto, especificamente alterações no preço. A classe abstrata `Observador` define a interface para observadores, e a classe `ObservadorPreco` é uma implementação concreta que exibe alertas quando o preço do produto muda. A classe `Produto` herda de `Sujeito`, que gerencia a lista de observadores e notifica-os quando o preço é alterado.

### Justificativa das Decisões

- O padrão Strategy foi escolhido para permitir que diferentes algoritmos de cálculo de preço possam ser aplicados sem modificar a classe Produto ou seus decoradores, promovendo a extensibilidade e o princípio aberto/fechado.
- O padrão Observer foi adotado para permitir que múltiplos componentes do sistema possam reagir a mudanças no estado do produto de forma desacoplada, facilitando a manutenção e a adição de novas funcionalidades reativas.

### Exemplo de Uso

```python
from decorators_pt import DecoratorDesconto, ObservadorPreco
from desktop import Desktop
from categoria import Categoria

cat = Categoria(1, "Eletrônicos")
desktop = Desktop("Dell XPS", "Preto", 3000.0, cat, "500W")

# Adicionar observador de preço
observador = ObservadorPreco()
desktop.anexar(observador)

# Aplicar desconto usando Strategy via Decorator
desktop_com_desconto = DecoratorDesconto(desktop, 15)  # 15% de desconto

print(desktop_com_desconto.getInformacoes())
desktop_com_desconto.cadastrar()

# Alterar preço para disparar notificação do observador
desktop.preco = 2700.0
```

### Testes

Testes unitários e de integração foram criados para validar o correto funcionamento dos padrões comportamentais, garantindo que as estratégias de preço sejam aplicadas corretamente e que as notificações sejam disparadas quando o preço muda.

---

## Conclusão

O projeto agora apresenta uma arquitetura robusta e flexível, utilizando padrões de projeto criacionais, estruturais e comportamentais para garantir a manutenção, extensibilidade e reutilização do código. A documentação e os testes abrangentes suportam a qualidade e a confiabilidade do sistema.
