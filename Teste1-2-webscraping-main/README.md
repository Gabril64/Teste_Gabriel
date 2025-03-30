# Teste1-2-webscraping

============================================

Este projeto tem como objetivo realizar web scraping para localizar e baixar arquivos de um site específico, seguido por um processo de transformação de dados para consolidar as informações extraídas.

============================================
# Funcionalidades

-  Web Scraping

-  Acessa o site-alvo para localizar os arquivos a serem baixados.

-  Identifica os anexos por meio da busca do texto "Anexo I" na página.

-  Realiza o download dos arquivos e compacta-os em formato .zip utilizando a biblioteca zipfile.

-  Repete o processo para outros anexos conforme necessário.

-  Transformação de Dados

-  Descompacta os arquivos baixados.

-  Extrai o anexo desejado.

-  Garantir que o nome de cada coluna no arquivo processado seja único.

-  Cria uma lista para armazenar as tabelas processadas.

-  Compactar o arquivo editado em um novo arquivo .zip chamado Teste_Gabriel.zip.

============================================

# Como Executar

1- Clone este repositório: 

  git clone https://github.com/seu-usuario/Teste1-2-webscraping.git

2- Instale as dependências necessárias:

  pip install -r requirements.txt

3- Execute o script de web scraping.

4- Execute o script de transformação de dados.
