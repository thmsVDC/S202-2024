from game import Game

def create_player(game):
    print('◊ ----- Criar jogador ----- ◊')
    name = input("Digite o nome do jogador: ")
    id = input("Digite o ID do jogador: ")
    game.create_player(name, id)
    print("Jogador criado com sucesso!")
    input("Aperte enter para continuar")

def update_player(game):
    print('◊ ----- Atualizar jogador ----- ◊')
    id = input("Digite o ID do jogador que deseja atualizar: ")
    new_name = input("Digite o novo nome do jogador: ")
    game.update_player(id, new_name)
    print("Jogador atualizado com sucesso!")
    input("Aperte enter para continuar")

def delete_player(game):
    print('◊ ----- Remover jogador ----- ◊')
    id = input("Digite o ID do jogador que deseja excluir: ")
    Game.delete_player(id)
    print("Jogador excluído com sucesso!")
    input("Aperte enter para continuar")

def create_match(game):
    print('◊ ----- Criar partida ----- ◊')
    match_id = input("Digite o ID da partida: ")
    players = input("Digite os IDs dos jogadores participantes separados por vírgula: ").split(',')
    result = input("Digite o resultado da partida: ")
    game.create_match(match_id, players, result)
    print("Partida criada com sucesso!")
    input("Aperte enter para continuar")

def get_player_matches(game):
    print('◊ ----- Histórico de partidas do jogador ----- ◊')
    player_id = input("Digite o ID do jogador: ")
    player_matches = game.get_player_matches(player_id)
    print(f"Histórico de partidas do jogador {player_id}:")
    for match_id, result in player_matches:
        print(f"ID da partida: {match_id}, Resultado: {result}")
    input("Aperte enter para continuar")

def get_match_info(game):
    match_id = input("Digite o ID da partida: ")
    match_info = game.get_match_info(match_id)
    print("Informações sobre a partida:")
    print("ID da partida:", match_info["match_id"])
    print("Resultado:", match_info["result"])
    print("Jogadores:")
    for player_id, name in match_info["players"]:
        print(f"ID do jogador: {player_id}, Nome do jogador: {name}")
    input("Aperte enter para continuar")

def get_all_players(game):
    players = game.get_all_players()
    print("Lista de todos os jogadores:")
    for player_id, name in players:
        print(f"ID do jogador: {player_id}, Nome do jogador: {name}")
    input("Aperte enter para continuar")


uri = "neo4j+s://718f53be.databases.neo4j.io"
user = "neo4j"
password = "BzyPklsNd57a4QS5iDNZtbpAgSqfhC5lEQmyWHQ1TFo"
game = Game(uri, user, password)

while True:
    print("\n◊ ----- Menu principal ----- ◊:")
    print("1. Criar jogador")
    print("2. Atualizar jogador")
    print("3. Excluir jogador")
    print("4. Criar partida")
    print("5. Histórico de partidas de um jogador")
    print("6. Informações sobre uma partida")
    print("7. Listar todos os jogadores")
    print("8. Sair")

    choice = input("Escolha uma opção: ")
    print('\n')

    if(choice == "1"):
            create_player(game)
    elif(choice == "2"):
            update_player(game)
    elif(choice == "3"):
            delete_player(game)
    elif(choice == "4"):
            create_match(game)
    elif(choice == "5"):
            get_player_matches(game)
    elif(choice == "6"):
            get_match_info(game)
    elif(choice == "7"):
            get_all_players(game)
    elif(choice == "8"):
            break
    else:
            print('Opção inválida. Tente novamente.')

game.db.close()
