from database import Database
from supermercado import Produtos
from helper.convertion import dict_to_doc
from helper.adm_search_helper import search_product

dbCounters = Database(database="fetin", collection="counters")
db = Database(database="fetin", collection="supermercado")
product = Produtos(db)

while True:
    print('\n' * 20)
    print('1. Adicionar produto')
    print('2. Buscar produto')
    print('3. Editar produto')
    print('4. Remover produto')
    print('5. Sair')
    choice = input('Digite uma opção: ')
    print('\n'*20)

    if choice == '1':
        nome = str(input('Nome: '))
        quantidadePorUnidade = str(input('quantidadePorUnidade: '))
        marca = str(input('Marca: '))
        quantidade = int(input('Quantidade: '))
        preco = float(input('Preço: '))
        tipo = str(input('Tipo: '))
        localizacao = str(input('Localização: '))

        product.create_product(nome, quantidadePorUnidade, marca, quantidade, preco, tipo, localizacao)
        input('\nAperte enter para continuar...')


    if choice == '2':
        search = str(input('Digite o que deseja procurar: '))

        results = product.search_product(search)
        documents = [dict_to_doc(d) for d in results]
        print(
            f'{'ID'.ljust(2)} | {'Nome'.ljust(20)} | {'Quantidade por produto'.ljust(22)} | {'Marca'.ljust(10)} | {'Quantidade'.ljust(10)} | {'Preço'.ljust(7)} | {'Tipo'.ljust(20)} | {'Setor'.ljust(20)} |')

        for doc in documents:
            print(
                f'{str(doc.id).ljust(2)} | {(doc.nome).ljust(20)} | {str(doc.quantidadePorUnidade).ljust(22)} | {(doc.marca).ljust(10)} | {str(doc.quantidade).ljust(10)} | R${str(doc.preco).ljust(5)} | {(doc.tipo).ljust(20)} | {(doc.localizacao).ljust(20)} |')

        input('\nAperte enter para continuar...')

    elif choice == '3':
        id_search = search_product()

        result = product.search_product("")
        document = dict_to_doc(result[0])
        print(
            f'{(document.id)} | {document.nome} | {document.quantidadePorUnidade} | {document.marca} | {document.quantidade} | R${document.preco} | {document.tipo} | {document.localizacao} |'
        )

        id = id_search
        nome = str(input('Nome: '))
        quantidadePorUnidade = str(input('quantidadePorUnidade: '))
        marca = str(input('Marca: '))
        quantidade = int(input('Quantidade: '))
        preco = float(input('Preço: '))
        tipo = str(input('Tipo: '))
        localizacao = str(input('Localização: '))

        product.edit_procuct(id, nome, quantidadePorUnidade, marca, quantidade, preco, tipo, localizacao)
        input('\nAperte enter para continuar...')

    elif choice == '4':
        search = search_product()
        product.delete_product(search)


    elif choice == '5':
        print('\n' * 20)
        print('Volte sempre!')
        break

    else:
        input('\nOpção inválida. Aperte enter para tentar novamente...')
