from database import Database
from motorista import Motorista
from corrida import Corrida
from passageiro import Passageiro
from bson.objectid import ObjectId

db = Database(database="exercicioAvaliativo1", collection="Motoristas")


class MotoristaCLI:
    def __init__(self, database):
        self.db = database

    def menu(self):
        while True:
            print('\n◊ ----- Bem-vindo -----◊')
            print('1. Cadastrar motorista')
            print('2. Editar motorista')
            print('3. Deletar motorista')
            print('4. Sair')
            choise = int(input('Insira uma opção: '))

            if choise == 1:
                print('◊ ----- Cadastrando novo motorista ----- ◊')
                passageiro = Passageiro(input('Digite o nome do passageiro: '),
                                        input('Digite o documento do passageiro: '))
                corrida = Corrida(int(input('Digite a nota da corrida: ')), passageiro)
                motorista = Motorista(input('Digite o nome do motorista: '), corrida)
                MotoristaDAO.criar_motorista(motorista.nome, corrida.nota, passageiro.nome, passageiro.documento)

                controle = input('Deseja adicionar mais corridas? [S/N]')
                while controle == 'S' or controle == 's':
                    MotoristaDAO.adicionar_corridas(motorista.nome)
                    controle = input('Deseja adicionar mais corridas? [S/N]')

            elif choise == 2:
                print('◊ ----- Editando motorista ----- ◊')
                idMotorista = input('Digite o ID do motorista: ')
                passageiro = Passageiro(input('Digite o nome do passageiro: '),
                                        input('Digite o documento do passageiro: '))
                corrida = Corrida(int(input('Digite a nota da corrida: ')), passageiro)
                motorista = Motorista(input('Digite o nome do motorista: '), corrida)

                MotoristaDAO.editar_motorista(idMotorista, motorista.nome, corrida.nota, passageiro.nome, passageiro.documento)
            elif choise == 3:
                print('◊ ----- Deletando motorista ----- ◊')
                id_motorista = input('Digite o ID do motorista: ')
                MotoristaDAO.deletar_motorista(id_motorista)

            elif choise == 4:
                print('Saindo...')
                break

            else:
                print('Opção inválida. Tente novamente.')


class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def criar_motorista(nome: str, nota_corrida: int, passageiro_nome: str, passageiro_doc: int):
        try:
            res = db.collection.insert_one({
                "nome": nome,
                'Corridas': [{
                    'nota': nota_corrida,
                    'Passageiros': {'nome': passageiro_nome, 'documento': passageiro_doc}
                }]
            })
            print(f"Motorista criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao adicionar um motorista: {e}")
            return None

    def adicionar_corridas(nome):
        try:
            passageiro = Passageiro(input('Digite o nome do passageiro: '),
                                    input('Digite o documento do passageiro: '))
            corrida = Corrida(int(input('Digite a nota da corrida: ')), passageiro)

            res = db.collection.update_one({'nome': nome},
                                           {'$push': {"Corridas": [{'nota': corrida.nota,
                                                                    'Passageiro': {'nome': passageiro.nome,
                                                                                   'documento': passageiro.documento
                                                                                   }}]}})
            print('Corrida adicionada com sucesso!')
        except Exception as e:
            print(f"Ocorreu um erro ao adicionar a corrida: {e}")
            return None

    def editar_motorista(id:str, nome: str, nota_corrida: int, passageiro_nome: str, passageiro_doc: int):
        try:
            res = db.collection.update_one({"_id": ObjectId(id)}, res = db.collection.update_one({{"_id": ObjectId(id)},
                                                                                                  {"$set": {"nome": nome,
                                                                                                            'Corridas':
                                                                                                                [{'nota': nota_corrida,
                                                                                                                  'Passageiros':
                                                                                                                      {'nome': passageiro_nome,
                                                                                                                       'documento': passageiro_doc}}]}}})
)
            print(f"Motorista atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"ocorreu um erro ao editar o motorista: {e}")
            return None

    def deletar_motorista(id: str):
        try:
            res = db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletado: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o motorista: {e}")
            return None
