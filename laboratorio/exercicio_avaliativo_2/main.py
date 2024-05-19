from query import Database, Query1, Query2
from teacher_crud import TeacherCRUD

db = Database("bolt://3.235.168.48:7687", "neo4j", "badge-aid-strips")
db.drop_all()

q1_db = Query1(db)
q2_db = Query2(db)
teacher_crud = TeacherCRUD(db)

print('◊ ----- Questão 1 ----- ◊')

# Busque pelo professor “Teacher” cujo nome seja “Renzo”, retorne o ano_nasc e o CPF.
print(q1_db.Renzo())

# Busque pelos professores “Teacher” cujo nome comece com a letra “M”, retorne o name e o cpf.
print(q1_db.initialM())

# Busque pelos nomes de todas as cidades “City” e retorne-os.
print(q1_db.cities())

# Busque pelas escolas “School”, onde o number seja maior ou igual a 150 e menor ou igual a 550, retorne o nome da
# escola, o endereço e o número.
print(q1_db.school())


print('◊ ----- Questão 2 ----- ◊')

# Encontre o ano de nascimento do professor mais jovem e do professor mais velho.
print(q2_db.profJovemeVelho())

# Encontre a média aritmética para os habitantes de todas as cidades, use a propriedade “population”.
print(q2_db.media())

# Encontre a cidade cujo CEP seja igual a “37540-000” e retorne o nome com todas as letras “a” substituídas por “A” .
print(q2_db.CEP())

# Para todos os professores, retorne um caractere, iniciando a partir da 3ª letra do nome.
print(q2_db.caracteres())


print('◊ ----- Questão 3 ----- ◊')

#Criar um "Teacher"
teacher_crud.create("Chris Lima", 1956, "189.052.396-66")

# Pesquisar o professor com o name de "Chris Lima" .
result = teacher_crud.read("Chris Lima")
print("Professor encontrado:")
print(result)

# Alterar o cpf do “Teacher” de name "Chris Lima" para "162.052.777-77" .
teacher_crud.update("Chris Lima", "162.052.777-77")

db.close()