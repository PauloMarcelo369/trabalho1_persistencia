#ALUNO: PAULO MARCELO CABRAL ARAÚJO -536813

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd


app = FastAPI(title="API CRUD de Produtos")


produtos_df = pd.DataFrame(columns=["id", "nome", "categoria", "preco"])

class Produto(BaseModel):
    id : int
    nome : str
    categoria : str
    preco : float


@app.get("/produtos")
def listar_produtos():
    return produtos_df.to_dict(orient="records")

@app.get("/produtos/{id}")
def obter_produto(id : int):
    global produtos_df
    produto = produtos_df.loc[produtos_df["id"] == id]
    if produto.empty:
        raise HTTPException(status_code=404, detail="Produto não foi encontrado")
    return produto.to_dict(orient="records")[0]

@app.post("/produtos")
def criar_produto(produto : Produto):
    global produtos_df
    if not produtos_df.loc[produtos_df["id"] == produto.id].empty:
        raise HTTPException(status_code=400, detail="Já existe um produto com este ID")
    novo = pd.DataFrame([produto.dict()])
    produtos_df = pd.concat([produtos_df, novo], ignore_index=True)
    return {"mensagem": "Produto cadastrado com sucesso!"}

@app.put("/produtos/{id}")
def atualizar_produto(id : int, produto : Produto):
    global produtos_df
    index = produtos_df.index[produtos_df["id"] == id].to_list()
    if not index:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    produtos_df.loc[index[0]] = [produto.id, produto.nome, produto.categoria, produto.preco]
    return {"mensagem": "Produto atualizado com sucesso!"}


@app.delete("/produtos/{id}")
def deletar_produto(id : int):
    global produtos_df
    index = produtos_df.index[produtos_df["id"] == id].to_list()
    if not index:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    produtos_df = produtos_df.drop(index[0])
    return {"mensagem": "Produto removido com sucesso!"}
