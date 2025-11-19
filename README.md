PI de Processamento de Livros (FastAPI/Pandas)
Este projeto é uma API REST que utiliza FastAPI para processar e limpar dados de livros em lote com a ajuda do Pandas.

🛠️ Configuração e Execução
Instale as dependências e inicie o servidor:

Instalação:



1. pip install fastapi uvicorn pandas pydantic
Execução do Servidor:



2. uvicorn main:app --reload
(O servidor rodará em http://127.0.0.1:8000)

3. Comando para Enviar Requisição (POST)
Use este comando no seu terminal PowerShell para enviar o arquivo e receber o JSON processado:

Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/catalogar-lote -ContentType 'application/json' -InFile .\dados_livros.json


Documentação: 
Acesse a URL abaixo para a documentação interativa (Swagger UI):[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

