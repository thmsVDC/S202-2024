from pymongo import MongoClient


class Document:
    def __init__(self, id, nome, quantidadePorUnidade, marca, quantidade, preco, tipo, localizacao):
        self.id = id
        self.nome = nome
        self.quantidadePorUnidade = quantidadePorUnidade
        self.marca = marca
        self.quantidade = quantidade
        self.preco = preco
        self.tipo = tipo
        self.localizacao = localizacao

    def __repr__(self):
        return (f"Documento(_id={self._id}, \
                nome='{self.nome}', \
                quantidadePorUnidade={self.quantidadePorUnidade}, \
                marca={self.marca}, \
                quantidade={self.quantidade}, \
                preco={self.preco}, \
                tipo={self.tipo}, \
                localizacao={self.localizacao})")


def dict_to_doc(dicionario):
    return Document(id=dicionario["_id"],
                    nome=dicionario["nome"],
                    quantidadePorUnidade=dicionario["quantidadePorUnidade"],
                    marca=dicionario["marca"],
                    quantidade=dicionario["quantidade"],
                    preco=dicionario["preco"],
                    tipo=dicionario["tipo"],
                    localizacao=dicionario["localizacao"])
