from database import GameDatabase

class Game:
    def __init__(self, uri, user, password):
        self.db = GameDatabase(uri, user, password)

    def create_player(self, name, player_id):
        self.db.create_player(name, player_id)

    def update_player(self, player_id, new_name):
        self.db.update_player(player_id, new_name)

    def delete_player(self, player_id):
        self.db.delete_player(player_id)

    def create_match(self, match_id, players, result):
        self.db.create_match(match_id, players, result)

    def get_player_matches(self, player_id):
        return self.db.get_player_matches(player_id)

    def get_match_info(self, match_id):
        return self.db.get_match_info(match_id)

    def get_all_players(self):
        return self.db.get_all_players()