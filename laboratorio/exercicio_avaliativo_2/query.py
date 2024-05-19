from neo4j import GraphDatabase


class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        data = []
        with self.driver.session() as session:
            results = session.run(query, parameters)
            for record in results:
                data.append(record)
            return data

    def drop_all(self):
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")


class Query1():
    def __init__(self, database):
        self.db = database

    def Renzo(self):
        query = """
        MATCH (t:Teacher {name: "Renzo"})
        RETURN t.ano_nasc, t.cpf
        """
        return self.db.execute_query(query)

    def initialM(self):
       query = """
       MATCH (t:Teacher)
       WHERE t.name STARTS WITH "M"
       RETURN t.name, t.cpf
       """
       results = self.db.execute_query(query)
       return [(result["name"], result["cpf"]) for result in results]

    def cities(self):
        query = """
        MATCH (c:City)
        RETURN c.name
        """
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def school(self):
        query = """
        MATCH (s:School)
        WHERE s.number >= 150 AND s.number <= 550
        RETURN s.name, s.address, s.number
        """
        results = self.db.execute_query(query)
        return [(result["name"], result["endereco"], result["numero"]) for result in results]

class Query2():
    def __init__(self, database):
        self.db = database

    def profJovemeVelho(self):
        query = """
        MATCH (t:Teacher)
        WITH t, t.ano_nasc AS birthYear
        ORDER BY birthYear
        RETURN COLLECT(t)[0].ano_nasc AS mais_jovem, COLLECT(t)[-1].ano_nasc AS mais_velho
        """
        return self.db.execute_query(query)

    def media(self):
        query = """
        MATCH (c:City)
        WITH AVG(c.population) AS media_populacao
        RETURN media_populacao
        """
        return self.db.execute_query(query)

    def CEP(self):
        query = """
        MATCH (c:City {cep: "37540-000"})
        RETURN REPLACE(c.name, "a", "A") AS nome_modificado
        """
        return self.db.execute_query(query)

    def caracteres(self):
        query = """
        MATCH (t:Teacher)
        RETURN SUBSTRING(t.name, 2, 1) AS terceira_letra
        """
        results = self.db.execute_query(query)
        return [result["terceira_letra"] for result in results]

