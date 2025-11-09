#ALUNO: PAULO MARCELO CABRAL ARAÚJO -536813

import httpx
import asyncio
import random

BASE_URL = "http://127.0.0.1:8000"

async def criar_produto(cliente, produto):
    resp = await cliente.post(
        f"{BASE_URL}/produtos", 
        json = {
                "nome":produto.get("nome"), 
                "categoria": produto.get("categoria"),
                "preco": produto.get("preco")
            }
        )
async def atualizar_produto(cliente): 
    minhalista = [u for u in range(3,30)]
    atualizado = {
                "nome": "Geladeira gamer",
                "categoria": "Eletrônicos",
                "preco": 5500.00
            }
    response = await cliente.put(f"{BASE_URL}/produtos/{random.choice(minhalista)}", json=atualizado)
    print("PUT:", response.json(),"\n\n")
async def deletar_produto(cliente):
    minhalista = [u for u in range(3,30)]
    response = await cliente.delete(f"{BASE_URL}/produtos/{random.choice(minhalista)}")
    print("DELETE:", response.json(),"\n\n")

async def executar_em_paralelo():
    minhalista = [u for u in range(3,30)]
    async with httpx.AsyncClient() as cliente:
        await asyncio.gather(
            criar_produto(cliente, {"nome": "Notebook Acer Aspire 5", "categoria": "Informática", "preco": 3500.00}),
            atualizar_produto(cliente),
            deletar_produto(cliente),
            criar_produto(cliente, {"nome": "Câmera de Segurança Intelbras Wi-Fi", "categoria": "Segurança", "preco": 350.00}),
            criar_produto(cliente, {"nome": "Smart TV Samsung 43\"", "categoria": "Eletrônicos", "preco": 2300.00}),
            deletar_produto(cliente),
            criar_produto(cliente, {"nome": "Mouse Logitech", "categoria": "Informática", "preco": 150.00}),
            atualizar_produto(cliente),
            deletar_produto(cliente),
            criar_produto(cliente, {"nome": "Fone Bluetooth JBL Tune 510BT", "categoria": "Áudio", "preco": 320.00}),
            criar_produto(cliente, {"nome": "Caixa de Som Alexa Echo Dot", "categoria": "Smart Home", "preco": 400.00}),
            atualizar_produto(cliente),
            criar_produto(cliente, {"nome": "Impressora HP DeskJet 2776", "categoria": "Informática", "preco": 420.00}),
            deletar_produto(cliente),
            criar_produto(cliente, {"nome": "Relógio Smartwatch Xiaomi Mi Band 8", "categoria": "Acessórios", "preco": 250.00}),
            atualizar_produto(cliente),
            deletar_produto(cliente),
            criar_produto(cliente, {"nome": "Teclado Mecânico Redragon Kumara", "categoria": "Informática", "preco": 280.00}),
            criar_produto(cliente, {"nome": "Motorola Moto G23", "categoria": "Eletrônicos", "preco": 1200.00}),
            atualizar_produto(cliente),
            deletar_produto(cliente),
            atualizar_produto(cliente),
            deletar_produto(cliente),
            atualizar_produto(cliente),
            deletar_produto(cliente),
            atualizar_produto(cliente),
            deletar_produto(cliente),
            atualizar_produto(cliente),
            deletar_produto(cliente),
            atualizar_produto(cliente)
        )


asyncio.run(executar_em_paralelo())
