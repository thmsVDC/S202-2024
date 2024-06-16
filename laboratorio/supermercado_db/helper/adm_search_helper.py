from database import Database
from supermercado import Produtos
from helper.convertion import dict_to_doc

db = Database(database="fetin", collection="supermercado")
product = Produtos(db)


def show_all_products(search):
    if isinstance(search, int):
        result = db.collection.find({'_id': search})
    else:
        regex_pattern = f'^{search}.*'
        result = db.collection.find({
            '$or': [
                {'nome': {'$regex': regex_pattern, '$options': 'i'}},
                {'tipo': {'$regex': regex_pattern, '$options': 'i'}},
                {'marca': {'$regex': regex_pattern, '$options': 'i'}}
            ]
        })
        return result

    if result:
        return result

    return print('Produto não encontrado')


def search_product():
    value = ''
    control = True
    while control:
        value = input("Digite o id, nome, marca ou tipo: ")

        try:
            num = int(value)
            value = num
        except ValueError:
            pass

        results = show_all_products(value)
        documents = [dict_to_doc(d) for d in results]
        for doc in documents:
            print(
                f'{str(doc.id).ljust(2)} | {(doc.nome).ljust(20)} | {str(doc.quantidadePorUnidade).ljust(5)} | {(doc.marca).ljust(10)} | {str(doc.quantidade).ljust(5)} | R${str(doc.preco).ljust(5)} | {(doc.tipo).ljust(20)} | {(doc.localizacao).ljust(20)} |')

        product_found = str(input('Produto encontrado? [S/N]'))
        if product_found == 'S' or product_found == 's':
            control = False

    print('\n----------')
    id_search = int(input('Digite o ID do produto: '))
    print('\n' * 20)

    return id_search



