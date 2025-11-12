#ALUNO: PAULO MARCELO CABRAL ARAÚJO -536813

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from threading import Lock

app = FastAPI(title="API CRUD de Produtos")

produtos_df = pd.read_csv("produtos.csv")
df_lock = Lock()
contador_id = int(produtos_df["id"].max()) + 1
class Produto(BaseModel):
    nome : str
    categoria : str
    preco : float


@app.get("/produtos")
def listar_produtos():
    return produtos_df.to_dict(orient="records")


@app.post("/produtos")
async def criar_produto(produto : Produto):
    global produtos_df,contador_id
    with df_lock:
        novo_produto = {
            "id": contador_id,
            "nome": produto.nome,
            "categoria": produto.categoria,
            "preco": produto.preco
        }
        contador_id += 1
        novo = pd.DataFrame([novo_produto])
        print(produtos_df)
        produtos_df = pd.concat([produtos_df, novo], ignore_index=True)
        print(produtos_df)
        produtos_df.to_csv("produtos.csv",index=False)
        return {"mensagem": "Produto cadastrado com sucesso!"}

@app.put("/produtos/{id}")
async def atualizar_produto(id : int, produto : Produto):
    global produtos_df
    with df_lock:
        index = produtos_df.index[produtos_df["id"] == id].to_list()
        if not index:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        produtos_df.loc[index[0]] = [id, produto.nome, produto.categoria, produto.preco]
        produtos_df.to_csv("produtos.csv",index=False)
        return {"mensagem": "Produto atualizado com sucesso!"}


@app.delete("/produtos/{id}")
async def deletar_produto(id : int):
    global produtos_df
    with df_lock:
        index = produtos_df.index[produtos_df["id"] == id].to_list()
        if not index:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        produtos_df = produtos_df.drop(index[0])
        produtos_df.to_csv("produtos.csv", index=False)
        return {"mensagem": "Produto removido com sucesso!"}

@app.get("/produtos/maior")
def produto_mais_caro():
    maior_preco = produtos_df["preco"].max()
    produto_maior = produtos_df[produtos_df["preco"] == maior_preco]
    return produto_maior.to_dict(orient="records")[0]


@app.get("/produtos/menor")
def produto_mais_barato():
    menor_preco = produtos_df["preco"].min()
    produto_menor = produtos_df[produtos_df["preco"] == menor_preco]
    return produto_menor.to_dict(orient="records")[0]


@app.get("/produtos/media")
def media_precos():
    media = produtos_df["preco"].mean()
    return {"media": media}


@app.get("/produtos/acima_media")
def produtos_acima_ou_igual_media():
    media = produtos_df["preco"].mean()
    produtos_acima = produtos_df[produtos_df["preco"] >= media]
    return produtos_acima.to_dict(orient="records")


@app.get("/produtos/abaixo_media")
def produtos_abaixo_media():
    media = produtos_df["preco"].mean()
    produtos_abaixo = produtos_df[produtos_df["preco"] < media]
    return produtos_abaixo.to_dict(orient="records")

@app.get("/produtos/{id}")
def obter_produto(id : int):
    global produtos_df
    produto = produtos_df.loc[produtos_df["id"] == id]
    if produto.empty:
        raise HTTPException(status_code=404, detail="Produto não foi encontrado")
    return produto.to_dict(orient="records")[0]
