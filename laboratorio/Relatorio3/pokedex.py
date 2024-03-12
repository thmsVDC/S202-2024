from database import Database

db = Database(database="pokedex", collection="pokemons")

class Pokedex:
  def __init__(self, database):
    self.database = database

  def encontrarPokemonPeloNome(nome: str):
    return db.collection.find({"name": nome})

  def encontrarPokemonPeloTipo(tipos: list):
    return db.collection.find({"type": {"$in": tipos}})
  
  def encontrarEvolucaoPokemon(nome: str):
    return db.collection.find({"name": nome, "next_evolution": {"$exists": True}})
  
  def encontrarFraquezas(fraquezas: list):
    return db.collection.find({"weaknesses": {"$all": fraquezas}})
  
  def chanceDeSpawn(a: float, b: float):
    return db.collection.find({"spawn_chance": {"$gt": a, "$lt": b}})