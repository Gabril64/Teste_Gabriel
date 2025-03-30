# Teste 4 - API

Conforme solicitado no Teste 4, foi criada uma API utilizando Flask no backend e Vue.js no frontend.

============================================
  BACKEND (Flask - Porta 5000)
============================================

Na pasta "backend", temos o código responsável pela inicialização do servidor Flask, que processa as requisições e retorna os dados mais relevantes.

O servidor realiza buscas e retorna as seguintes colunas do relatório:

- Razão Social
- Nome Fantasia
- CNPJ
- Modalidade
- Cidade
- UF

============================================
  FRONTEND (Vue.js - Porta 5173)
============================================

Na pasta "frontend", está a parte gráfica da aplicação, responsável por renderizar os dados e interagir com o usuário.

-  Para iniciar o frontend, utilize o comando:
   npm run dev

O principal arquivo é "Busca.vue", que gerencia a interface da aplicação e a comunicação com o backend por meio do seguinte comando:

   axios.get('http://localhost:5000/buscar')

Esse comando permite que o frontend envie requisições para o backend e exiba os resultados na tela.

============================================
  INSTRUÇÕES PARA EXECUÇÃO
============================================

1    Iniciar o backend:
   - Acesse a pasta principal e execute:
     python app.py

2️    Iniciar o frontend:
   - Acesse a pasta "vue-frontend" e execute:
     npm run dev

3️    Acesse a aplicação no navegador:
   - http://localhost:5173

============================================
  Coleção Postman
============================================

  https://gabril64.postman.co/workspace/Gabril64's-Workspace~6123555e-c1d8-4de7-8728-7e076d0deca6/collection/43596617-443d8ba7-0d34-4907-bb58-9e9b973dff91?action=share&creator=43596617
