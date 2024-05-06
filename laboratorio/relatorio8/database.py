from neo4j import GraphDatabase


class GameDatabase:
    def __init__(self, uri, user, password):
        self._uri = uri
        self._user = user
        self._password = password
        self._driver = GraphDatabase.driver(self._uri, auth=(self._user, self._password))

    def close(self):
        self._driver.close()

    # Criando os players
    def create_player(self, name, player_id):
        with self._driver.session() as session:
            session.run("CREATE (p:Player {name: $name, player_id: $player_id})", name=name, player_id=player_id)

    # Atualizando os players
    def update_player(self, player_id, new_name):
        with self._driver.session() as session:
            session.run("MATCH (p:Player {player_id: $player_id}) SET p.name = $new_name", player_id=player_id,
                        new_name=new_name)

    # Deletando os players
    def delete_player(self, player_id):
        with self._driver.session() as session:
            session.run("MATCH (p:Player {player_id: $player_id}) DETACH DELETE p", player_id=player_id)

    # Criando uma partida
    def create_match(self, match_id, players, result):
        with self._driver.session() as session:
            session.run("CREATE (m:Match {match_id: $match_id, result: $result})", match_id=match_id, result=result)
            for player_id in players:
                session.run("MATCH (p:Player {player_id: $player_id}), (m:Match {match_id: $match_id}) "
                            "CREATE (p)-[:PARTICIPATED_IN]->(m)", player_id=player_id, match_id=match_id)

    # Colocando os players na partida
    def get_player_matches(self, player_id):
        with self._driver.session() as session:
            result = session.run("MATCH (p:Player {player_id: $player_id})-[:PARTICIPATED_IN]->(m:Match) "
                                 "RETURN m.match_id AS match_id, m.result AS result", player_id=player_id)
            return [(record["match_id"], record["result"]) for record in result]

    # Informações da partida
    def get_match_info(self, match_id):
        with self._driver.session() as session:
            result = session.run("MATCH (m:Match {match_id: $match_id})<-[:PARTICIPATED_IN]-(p:Player) "
                                 "RETURN p.player_id AS player_id, p.name AS name, m.result AS result",
                                 match_id=match_id)
            players = [(record["player_id"], record["name"]) for record in result]
            match_info = {"match_id": match_id, "players": players}
            return match_info

    # Mostrando todos os players
    def get_all_players(self):
        with self._driver.session() as session:
            result = session.run("MATCH (p:Player) RETURN p.player_id AS player_id, p.name AS name")
            return [(record["player_id"], record["name"]) for record in result]