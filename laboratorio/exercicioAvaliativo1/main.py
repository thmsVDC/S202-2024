from database import Database
from motoristaDao import MotoristaDAO, MotoristaCLI
import motorista
import corrida
import passageiro

db = Database(database="exercicioAvaliativo1", collection="Motoristas")
#db.resetDatabase()

cli = MotoristaCLI(db)
cli.menu()
