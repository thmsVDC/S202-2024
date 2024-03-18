from database import Database

db = Database(database="mercado", collection="compras")

class ProductAnalyzer():
  def __init__(self, database):
    self.database = database

  def totalVendas():
    return db.collection.aggregate([
      {"$unwind": "$produtos"},
      {"$group": {"_id": "$data_compra", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}
    ])

  def produtoMaisVendido():
    return db.collection.aggregate([
      {"$unwind": "$produtos"},
      {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}
      }},
      {"$sort": {"total": -1}},
      {"$limit": 1}
    ])

  def clienteMaisGastou():
    return db.collection.aggregate([
      {"$unwind": "$produtos"},
      {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
      {"$sort": {"total": -1}},
      {"$limit": 1}
    ])

  def maisDe1Vendido():
    return db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$match": {"produtos.quantidade": {"$gt": 1}}},  # Modificado para considerar mais de uma unidade vendida
        {"$group": {
            "_id": "$cliente_id",
            "produtos_vendidos": {"$push": "$produtos"}, 
        }}
    ])

