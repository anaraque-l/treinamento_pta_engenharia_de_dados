# main.py
import pandas as pd # tratar os dados 
import uvicorn 
from pydantic import BaseModel #contrato de conversão. 
from typing import List, Optional # usado para definir as litas e campos que podem ser nulos. 
from fastapi import FastAPI 


# configuração inicial 

#inicialização do fastapi 
app = FastAPI(title="API tratamento de dados da biblioteca ") 



# contrato de dados de entrada

#Modelo de entrada: livro sujo 

class LivroSujo(BaseModel): 
    titulo : str 
    autor : str
    #optinal int define para FASTaPI que o campo é opcional e deve ser inteiro. 
    ano_publicacao : Optional[int] = None 

#Modelo de saída: livro limpo 

class LivroLimpo(BaseModel):
    titulo_formatado : str 
    autor_formatado : str
    ano_tratado : int 
    classificacao : str




#Rota em Lote : 
@app.post("/catalogar-lote", response_model= List[LivroLimpo])
def catalogar_lote(livros_sujos:list[LivroSujo]):
    
# pydantic .model_dump() que transforma um objeto em um dicionario. 

    dados = [livro.model_dump() for livro in livros_sujos]
#table apara acessar o lote
    df = pd.DataFrame(dados)
    
    #todas as linhas 
    df['titulo_formatado'] = df['titulo'].str.strip().str.title()

    df['autor_formatado'] = df['autor'].str.upper().str.strip() # CORREÇÃO: Usando 'autor_formatado' para corresponder ao modelo LivroLimpo

    #Anos de publicação nulos como um ano padrão. 

    df['ano_tratado'] = df['ano_publicacao'].fillna(2025).astype(int) # CORREÇÃO: Usando 'ano_tratado' para corresponder ao modelo LivroLimpo e convertendo para int

    #Anos negativos 

    df.loc[df['ano_tratado'] < 0, 'ano_tratado'] = 2025

    # Lógica de Classificação

    
    df['classificacao'] = ['Clássico' if ano < 2000 else 'Moderno' for ano in df['ano_tratado']]
    
    

    # Dataframe -> lista de dicionários (json) 
    # 'orient = "records" essencial para formatar como lista de jsons que o fastapi api espera. 

    return df[['titulo_formatado', 'autor_formatado', 'ano_tratado', 'classificacao']].to_dict(orient="records") 