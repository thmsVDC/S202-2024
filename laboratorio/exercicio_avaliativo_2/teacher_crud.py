class TeacherCRUD:
    def __init__(self, db):
        self.db = db

    def create(self, name, ano_nasc, cpf):
        query = f"""
        CREATE (t:Teacher {{name: "{name}", ano_nasc: {ano_nasc}, cpf: "{cpf}"}})
        """
        self.db.execute_query(query)

    def read(self, name):
        query = f"""
        MATCH (t:Teacher {{name: "{name}"}})
        RETURN t
        """
        return self.db.execute_query(query)

    def delete(self, name):
        query = f"""
        MATCH (t:Teacher {{name: "{name}"}})
        DELETE t
        """
        self.db.execute_query(query)

    def update(self, name, new_cpf):
        query = f"""
        MATCH (t:Teacher {{name: "{name}"}})
        SET t.cpf = "{new_cpf}"
        """
        self.db.execute_query(query)