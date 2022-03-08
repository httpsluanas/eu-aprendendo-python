menuInicial = ["Produtos", "Carrinho de Compras"]
menuAddProdutos = ["Voltar", "Macarrão " + "(R$ 5.99)", "Leite " + "(R$ 4.56)", "Arroz " + "(R$ 7.20)", "Banana " + "(R$ 4.50)", "Cerveja " + "(R$ 3.50)", "Café " + "(R$ 10.30)"]
carrinhoDeCompras = ["Voltar", "Lista de Produtos"]
listaProduto = []
listaPreco = []
listaFinalizar = ["Voltar ao início", "Finalizar pedido"]


def enumerarListas(nomeLista):
    for i, item in enumerate(nomeLista):
        print(i, "-", item)


def indiceProduto(y):
    return menuAddProdutos[y]


def opAddProduto(x):
    while x > 0:
        x = int(input("Adicione os produtos que você deseja no carrinho ou volte para o início. Após "
                      "adicionar, digite 0 para voltar: "))
        if x > 6:
            numeroInvalido()
        if x == 0:
            menu1(menuInicial)
        produtosCarrinho = indiceProduto(x)
        listaProduto.append(produtosCarrinho)


def numeroInvalido():
    print("Número inválido.")
    print("----------")
    menu1(menuInicial)


def menu1(lista):
    enumerarListas(lista)
    escolha1 = int(input(""))
    if escolha1 == 0:
        enumerarListas(menuAddProdutos)
        addProduto = 1
        opAddProduto(addProduto)
    elif escolha1 == 1:
        enumerarListas(carrinhoDeCompras)
        listaProdOuValor = int(input("Veja sua lista de produtos e acesse o valor total: "))
        if listaProdOuValor == 0:
            menu1(menuInicial)
        elif listaProdOuValor == 1:
            enumerarListas(listaProduto)
            print("----------")
            for i, item in enumerate(listaProduto):
                dividirPreco = item.split()
                preco = dividirPreco[2]
                praRemover = ")"
                preco = ''.join(x for x in preco if x not in praRemover)
                precoFloat = float(preco)
                listaPreco.append(precoFloat)
            soma = 0
            for item in listaPreco:
                soma += item
            print("Valor total: R$", soma)
            print("----------")
            enumerarListas(listaFinalizar)
            finalizarPedido = (int(input("Escolha uma opção: ")))
            if finalizarPedido == 0:
                menu1(menuInicial)
            elif finalizarPedido == 1:
                print("----------")
                for i, item in enumerate(listaProduto):
                    print(item)
                print()
                print("TOTAL R$      ", soma)
                print("----------")
        else:
            numeroInvalido()

    else:
        numeroInvalido()


print("Bem vindo! Escolha uma opção: ")
menu1(menuInicial)

print()
