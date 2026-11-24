from itens import itens

categorias_acoes = {
    "alimentar": "alimentos",
    "brincar": "brinquedos",
    "limpar": "higiene",
    "medicar": "medicamentos"
}

def listar_itens_disponiveis(pet, categoria):
    numero = 1
    print("-" * 50)
    print("ITENS DIPONIVEIS".center(50))
    print("-" * 50)
    if not pet["inventario"]:
        print("Inventário vazio!\n")
    else:
            for item_catalogo, dados in itens[categoria].items():
                    if item_catalogo in pet["inventario"]:
                        numero += 1
                        print(f"{numero} - {item_catalogo.replace("_"," ").title()}\nUsos: {pet["inventario"][item_catalogo]}") 
                        for efeito, quantia in dados.items():
                            if efeito == "usos" or efeito == "preco":
                                continue
                            else:
                                if quantia is True:
                                    print(f"Efeito: {efeito.replace("_", " ").title()}\n")
                                else:
                                    print(f"Efeito: {efeito.replace("_", " ").title()} | Beneficio: {quantia} pontos\n")


def selecionar_item(pet, categoria):
    listar_itens_disponiveis(pet, categoria)
    while True:
        if not pet["inventario"]:
            return
        try:
            itens_no_inv = []
            for item_catalogo in itens[categoria]:
                if item_catalogo in pet["inventario"]:
                    itens_no_inv.append(item_catalogo)
            if not itens_no_inv:
                print("O inventario está vazio")
                return
            item_selecionado = int(input("Selecione o item que deseja utilizar: \n"))  
            if 1 <= item_selecionado <= len(itens_no_inv):
                item_escolhido = itens_no_inv[item_selecionado - 1]
                return item_escolhido
            else:
                print("Você precisa selecionar uma opção valida\n")
                continue
        except ValueError:
            print("Você precisa selecionar uma opção valida\n")
            continue

def consumir_item(pet, item_escolhido):
    if pet["inventario"][item_escolhido] >= 1:
        pet["inventario"][item_escolhido] -= 1
        if pet["inventario"][item_escolhido] == 0:
            pet["inventario"].pop(item_escolhido)
            print(f"Item consumido com sucesso!\nOs usos do item se esgotaram")
        else:  
            print(f"Item consumido com sucesso!\nRestam {pet["inventario"][item_escolhido]} usos")
    else:
        print(f"O item selecionado não tem mais usos disponiveis")
        pet["inventario"].pop(item_escolhido)

def utilizar_item(pet):
    item = selecionar_item(pet)
    if item is None:
        return
    if item == "curativo":
        if not pet["doente"]:
            print(f"O {pet["nome"].title()} não está doente")
            return
    aplicar_efeito(pet, item)
    consumir_item(pet, item)
    

def aplicar_efeito(pet, item_escolhido):
    for categoria in itens.values():
        if item_escolhido in categoria:
            dados = categoria[item_escolhido]
            for chave, valor in dados.items():
                if chave == "preco" or chave == "usos":
                    continue
                else:
                    if valor is True:
                            print(f"Efeito: {chave.replace("_", " ")}")
                            pet["doente"] = False
                    else:
                        print(f"Efeito: {chave.replace("_", " ")} | Quantia: {valor} pontos")
                        if chave == "fome_recuperada":
                            pet["fome"]= min(pet["fome"] + valor, 100)
                        if chave == "higiene_recuperada":
                            pet["higiene"]= min(pet["higiene"] + valor, 100)
                        if chave == "felicidade_recuperada":
                            pet["felicidade"]= min(pet["felicidade"] + valor, 100)
                        if chave == "saude_recuperada":
                            pet["saude"]= min(pet["saude"] + valor, 100)
                    


