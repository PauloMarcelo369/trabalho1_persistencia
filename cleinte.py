#ALUNO: PAULO MARCELO CABRAL ARAÚJO -536813

import httpx
import asyncio
BASE_URL = "http://127.0.0.1:8000"


novo_produto = {
    "nome": "Notebook",
    "categoria": "Eletrônicos",
    "preco": 3500.00
}

async def criar_produto():
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/produtos", json=novo_produto)
        print("POST status:", response.status_code)
        try:
            print("POST body:", response.json(),"\n\n")
        except Exception:
            print("Resposta não-JSON:", response.text)
        atualizado = {
            "nome": "Notebook Gamer",
            "categoria": "Eletrônicos",
            "preco": 5500.00
        }
        response = await client.put(f"{BASE_URL}/produtos/1", json=atualizado)
        print("PUT:", response.json(),"\n\n")
        response = await client.delete(f"{BASE_URL}/produtos/1")
        print("DELETE:", response.json(),"\n\n")

response = httpx.get(f"{BASE_URL}/produtos")
print("GET todos:", response.json(),"\n\n")

response = httpx.get(f"{BASE_URL}/produtos/maior")
print("GET maior:", response.json(),"\n\n")

response = httpx.get(f"{BASE_URL}/produtos/menor")
print("GET menor:", response.json(),"\n\n")

response = httpx.get(f"{BASE_URL}/produtos/media")
print("GET media:", response.json(),"\n\n")

response = httpx.get(f"{BASE_URL}/produtos/acima_media")
print("GET acima ou igual da media:", response.json(),"\n\n")

response = httpx.get(f"{BASE_URL}/produtos/abaixo_media")
print("GET abaixo da media:", response.json(),"\n\n")

response = httpx.get(f"{BASE_URL}/produtos/1")
print("GET ID 1:", response.json(),"\n\n")

response = httpx.get(f"{BASE_URL}/produtos")
print("Lista final:", response.json(),"\n\n")

asyncio.run(criar_produto())