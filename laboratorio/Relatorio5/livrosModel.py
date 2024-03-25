from pymongo import MongoClient
from bson.objectid import ObjectId
from database import Database

db = Database(database="Relatorio5", collection="Livros")

class livroModel:
    def __init__(self, database):
        self.db = database

    def criar_livro(self, titulo: str, autor:str, ano:int, preco:float):
        try:
            res = self.db.collection.insert_one({"titulo": titulo, "autor": autor, "ano": ano, "preco": preco})
            print(f"Livro criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao adicionar um livro: {e}")
            return None

    def procurar_livro_por_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Livro encontrado: {res}")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao procurar um livro: {e}")
            return None

    def editar_livro(self, id: str, titulo: str, autor: int, ano:int, preco:float):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco}})
            print(f"Livro atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"ocorreu um erro ao editar o livro: {e}")
            return None

    def deletar_livro(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Livro deletado: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o livro: {e}")
            return None