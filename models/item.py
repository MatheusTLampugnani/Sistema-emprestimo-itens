import json
import os

class Item:
    DATA_FILE = "data/itens.json"

    def __init__(self, nome, codigo, disponivel=True):
        self.nome = nome
        self.codigo = codigo
        self.disponivel = disponivel

    def to_dict(self):
        return {"nome": self.nome, "codigo": self.codigo, "disponivel": self.disponivel}

    @staticmethod
    def salvar_item(item):
        itens = Item.carregar_itens()
        itens.append(item.to_dict())
        Item._salvar_em_arquivo(itens)

    @staticmethod
    def carregar_itens():
        if not os.path.exists(Item.DATA_FILE):
            return []
        with open(Item.DATA_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def atualizar_itens(itens):
        Item._salvar_em_arquivo(itens)

    @staticmethod
    def _salvar_em_arquivo(itens):
        with open(Item.DATA_FILE, "w") as f:
            json.dump(itens, f, indent=4)
