#ALUNO: PAULO MARCELO CABRAL ARAÚJO -536813

import httpx

BASE_URL = "http://127.0.0.1:8000"


novo_produto = {
    "id": 1,
    "nome": "Notebook",
    "categoria": "Eletrônicos",
    "preco": 3500.00
}

response = httpx.post(f"{BASE_URL}/produtos", json=novo_produto)
print("POST:", response.json())


response = httpx.get(f"{BASE_URL}/produtos")
print("GET todos:", response.json())

response = httpx.get(f"{BASE_URL}/produtos/1")
print("GET ID 1:", response.json())

atualizado = {
    "id": 1,
    "nome": "Notebook Gamer",
    "categoria": "Eletrônicos",
    "preco": 5500.00
}
response = httpx.put(f"{BASE_URL}/produtos/1", json=atualizado)
print("PUT:", response.json())

response = httpx.delete(f"{BASE_URL}/produtos/1")
print("DELETE:", response.json())

response = httpx.get(f"{BASE_URL}/produtos")
print("Lista final:", response.json())
