from itens import itens

def comprar_item(pet, categoria, produto):
    dados = itens[categoria][produto]
    if pet["moedas"] < dados["preco"]:
        print("Você não tem moedas suficientes, a compra não foi realizada\n")
        return False
    else:
        pet["moedas"] -= dados["preco"]
        if produto in pet["inventario"]:
            pet["inventario"][produto] += dados["usos"]
        else:
            pet["inventario"][produto] = dados["usos"]
        return True
    
def consultar_item():
   item = input("Digite o nome do item que deseja consultar aqui: ").strip().lower().replace(' ', '_')
   encontrado = False
   for categoria, lista_itens in itens.items():
        if item in lista_itens:
            encontrado = True
            dados = lista_itens[item]
            preco = dados.get("preco")
            print(f"Item: {item.replace('_', ' ').title()}\nCategoria: {categoria.title()}\nPreço: {preco}")
            usos = dados.get("usos")
            print(f"Usos: {usos}\n")
            for chave, valor in dados.items():
                if chave in ("usos","preco"):
                    continue
                else:
                 print(f"Efeito: {chave.replace('_', ' ').title()} = {valor}")

   if not encontrado:
    print("Item não encontrado!")

def consultar_inventario(pet):
    print("=" * 50)
    print("INVENTÁRIO".center(50))
    print("=" * 50)
    if not pet["inventario"]:
        print("Inventário vazio!\n")
    else:
        for chave, valor in pet["inventario"].items():
            print(f"{chave.replace("_"," ").title().center(20)}\nUsos disponíveis: {str(valor).center(20)}\n")


def consultar_catalogo(pet):
    print("-" * 50)
    print("CATÁLOGO PIXEL PET".center(50))
    print("-" * 50)
    print(f"Moedas: {pet["moedas"]}\n")
    categorias = list(itens.keys()) 
    while True:
        try:
            for numero, categoria in enumerate(categorias, start=1):
                print(f"{numero} - {categoria.title()}\n")
            print("0 - Para voltar ao menu principal\n")
            categoria_escolhida = int(input("Escolha qual categoria deseja acessar: \n"))
            if categoria_escolhida == 0:
                break
            elif categoria_escolhida < 1 or categoria_escolhida > len(categorias):
                print("Você precisa escolher uma opção válida!\n")
                continue
        except ValueError:
            print("Você precisa escolher uma opção válida!\n")
            continue
        categoria = categorias[categoria_escolhida-1]
        produtos = list(itens[categoria].keys())
        while True:
            try:
                for numero, (nome_item, dados) in enumerate(itens[categoria].items(), start=1):
                    print(f"{numero} - {nome_item}\n{dados["preco"]} moedas | {dados["usos"]} usos\n")
                    for efeito, quantia in dados.items():
                        if efeito == "preco" or efeito == "usos":
                            continue
                        else:
                            if quantia is True:
                                print(f"Efeito: {efeito.replace("_", " ").title()}\n")
                            else:
                                print(f"Efeito: {efeito.replace("_", " ").title()} | Beneficio: {quantia} pontos\n")
                print("0 - Voltar às categorias\n")
                    
                    
                produto_escolhido = int(input("Escolha o produto que deseja: \n"))
                if produto_escolhido == 0:
                    break
                elif produto_escolhido < 1 or produto_escolhido > len(produtos):
                    print("Você precisa escolher uma opção válida!\n")
                    continue
                produto = produtos[produto_escolhido - 1]
                dados = itens[categoria][produto]
                compra_realizada = comprar_item(pet, categoria, produto)
                if compra_realizada:
                    print(f"Compra confirmada!\nProduto: {produto.replace("_", " ").title()}\nUsos recebidos: {dados["usos"]}\nSaldo de moedas: {pet["moedas"]}\n")
                else:
                    print("Moedas insuficientes a compra não foi realizada\n")
                    continue
            
            except ValueError:
                print("Você precisa escolher uma opção válida!\n")
                continue


def menu_loja(pet):
    while True:
        print("-" * 50)
        print("MENU PIXEL PET".center(50))
        print("-" * 50)       
        print(f"Moedas: {pet["moedas"]}\n")
        print("1 - Consultar catálogo de itens")
        print("2 - Consultar inventário")
        print("3 - Pesquisar item específico")
        print("4 - Para fechar o jogo")
        print("-" * 50)
        try:
            acao = int(input("Escolha uma opção: "))

            if acao == 1:
                consultar_catalogo(pet)
            elif acao == 2:
                consultar_inventario(pet)
            elif acao == 3:
                consultar_item()
            elif acao == 4:
                break
            else:
                print("opção invalida!\n")
        except ValueError:
            print("Você precisa escolher uma opção válida!\n")
            

