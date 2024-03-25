from database import Database
from livrosModel import livroModel

db = Database(database="Relatorio5", collection="Livros")
livro = livroModel(db)


controle = True
while(controle):
  print("|--------------------|")
  print("(1) Adicionar um livro")
  print("(2) Procurar um livro")
  print("(3) Editar um livro")
  print("(4) Deletar um livro")
  print("(5) Sair do programa")
  print("|--------------------|")
  op = int(input("Selecione uma das opções acima: "))
  print("\n")
  
  if(op == 1):
    titulo = str(input("Digite o titulo: "))
    autor = str(input("Digite o nome do autor: "))
    ano = int(input("Digite o ano de lançamento: "))
    preco = float(input("Digite o preço do livro: "))
    livro.criar_livro(titulo, autor, ano, preco)

  if(op == 2):
    idProcura = str(input("Digite o id que deseja procurar: "))
    livro.procurar_livro_por_id(idProcura)

  if(op == 3):
    _id = str(input("Digite o id do livro: "))
    titulo = str(input("Digite o titulo: "))
    autor = str(input("Digite o nome do autor: "))
    ano = int(input("Digite o ano de lançamento: "))
    preco = float(input("Digite o preço do livro: "))
    livro.editar_livro(_id, titulo, autor, ano, preco)

  if(op == 4):
    idDeleta = str(input("Digite o id do livro que você quer deletar: "))
    livro.deletar_livro(idDeleta)

  if(op == 5):
    controle = False