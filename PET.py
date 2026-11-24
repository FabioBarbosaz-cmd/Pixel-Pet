
def criar_pet():
    while True:
        nome = input("Digite o nome do seu pet aqui: ").strip()
        if nome == "":
         print("Você não digitou um nome valído, tente novamente!")
        else:
           break
    pet = {
    "nome": nome,
    "fome": 100,
    "energia": 100,
    "saude": 100,
    "felicidade":100,
    "higiene": 100,
    "moedas": 100,
    "doente": False,
    "inventario": {}
}
    return pet

def mostrar_status(pet):
   for chave, valor in pet.items():
    if chave == "doente":
      continue
    if isinstance(valor, int):
        print(f"{chave.title()}: {valor}")
    elif isinstance(valor, str):
        print(f"{chave.title()}: {valor.title()}")


