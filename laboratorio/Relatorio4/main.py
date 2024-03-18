from analiseProdutos import ProductAnalyzer
from helper.writeAJson import writeAJson
from database import Database


db = Database(database="mercado", collection="compras")
#db.resetDatabase()

totalGasto = ProductAnalyzer.totalVendas()
writeAJson(totalGasto, "Total gasto por dia")

produtoMaisVendido = ProductAnalyzer.produtoMaisVendido()
writeAJson(produtoMaisVendido, "Produto mais vendido")

clienteMaisGastou = ProductAnalyzer.clienteMaisGastou()
writeAJson(clienteMaisGastou,"Cliente que mais gastou")

maisDe1Vendido = ProductAnalyzer.maisDe1Vendido()
writeAJson(maisDe1Vendido, "Produto mais de 1 unidade vedido")