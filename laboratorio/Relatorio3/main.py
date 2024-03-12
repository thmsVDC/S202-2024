from database import Database
from helper.writeAJson import writeAJson
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")
#db.resetDatabase()

pikachu = Pokedex.encontrarPokemonPeloNome("Pikachu")
writeAJson(pikachu, "pikachu")

tipos = ["Fighting"]
pokemons = Pokedex.encontrarPokemonPeloTipo(tipos)
writeAJson(pokemons, "pokemons_por_tipos")

Bulbasaur = Pokedex.encontrarEvolucaoPokemon("Bulbasaur")
writeAJson(Bulbasaur, "evolucao_do_pokemon")

fraquezas = ["Electric","Grass"]
pokemonsFraq = Pokedex.encontrarFraquezas(fraquezas)
writeAJson(pokemonsFraq, "fraquezas_pokemons")

a = 0.3
b = 0.6
chanceSpawn = Pokedex.chanceDeSpawn(a, b)
writeAJson(chanceSpawn, "chance_spawn")

