from acoes import utilizar_item

pet_teste = {
    "nome": "Pipoca",
    "fome": 95,
    "energia": 100,
    "saude": 50,
    "felicidade": 100,
    "higiene": 100,
    "doente": True,
    "inventario":{
    "racao": 12,
    "bola_basica": 12
}
    }


utilizar_item(pet_teste)

print(pet_teste)