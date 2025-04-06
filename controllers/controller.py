from models.item import Item
from models.pessoa import Pessoa
from models.emprestimo import Emprestimo
from datetime import datetime

class Controller:

    @staticmethod
    def cadastrar_item(nome, codigo):
        item = Item(nome, codigo)
        Item.salvar_item(item)
        print("Item cadastrado com sucesso!")

    @staticmethod
    def cadastrar_pessoa(nome, cpf):
        pessoa = Pessoa(nome, cpf)
        Pessoa.salvar_pessoa(pessoa)
        print("Pessoa cadastrada com sucesso!")

    @staticmethod
    def registrar_emprestimo(codigo_item, cpf):
        itens = Item.carregar_itens()
        for item in itens:
            if item["codigo"] == codigo_item and item["disponivel"]:
                item["disponivel"] = False
                Item.atualizar_itens(itens)

                emprestimo = Emprestimo(codigo_item, cpf, datetime.now().strftime("%d/%m/%Y"))
                Emprestimo.salvar_emprestimo(emprestimo)
                print("Empréstimo registrado com sucesso!")
                return

        print("Item não encontrado ou indisponível.")

    @staticmethod
    def registrar_devolucao(codigo_item):
        emprestimos = Emprestimo.carregar_emprestimos()
        for emp in emprestimos:
            if emp["codigo_item"] == codigo_item and not emp["devolvido"]:
                emp["devolvido"] = True
                Emprestimo.atualizar_emprestimos(emprestimos)

                itens = Item.carregar_itens()
                for item in itens:
                    if item["codigo"] == codigo_item:
                        item["disponivel"] = True
                        break
                Item.atualizar_itens(itens)
                print("Devolução registrada com sucesso!")
                return

        print("Empréstimo não encontrado.")

    @staticmethod
    def listar_itens():
        itens = Item.carregar_itens()
        print("\nItens Disponíveis:")
        for item in itens:
            if item["disponivel"]:
                print(f"{item['codigo']} - {item['nome']}")

        print("\nItens Emprestados:")
        for item in itens:
            if not item["disponivel"]:
                print(f"{item['codigo']} - {item['nome']}")
