# Scripts-Dados-Loteria  
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)
![Static Badge](https://img.shields.io/badge/license-mit-%235CE500?style=for-the-badge)
## Descrição
Este reepositório tem finalidade mostrar como, usando python, podemos capturar dados de um arquivo .xlsx e armazenar os dados em um banco de dados.  
Os Scripts foram criados pensando nas loterias caixa para os sorteios Mega-Sena Quina LotoFácil e Milionária  
<h3 align="center"> Demonstração </h3>  
<p align="center"><img src="https://github.com/SrJohn369/Scripts-Dados-Loteria/assets/106630200/b819202b-4b29-4651-98b8-73546910a0ea"></p>

## :computer:Tecnologias
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![SQLALCHEMY](https://img.shields.io/badge/SQLAlchemy-%23D71F00?style=for-the-badge&logo=sqlalchemy)
![PostgreSQL](https://img.shields.io/badge/postgresql-%234169E1?style=for-the-badge&logo=postgresql&logoColor=%23FFF)  
![Static Badge](https://img.shields.io/badge/windows%2011-%230078D4?style=flat-square&logo=windows&logoColor=%23FFF)
## Funções Principais
Estas funções estarão presentes em todos os scripts de `/funcs`, sofrendo adaptações e cada um deles.  
  
`criar_dataFrame()`: Esta função irá capturar todos os dados do arquivo .xlsx e criará um dicionário com todos os dados.  
`adicionar_dados()`: Esta função deverá criar tabelas caso não exista e armazenar os dados nesta tabela. A função irá dar dados de status de cada linha ou colunas adicionadas de acordo com o script que está sendo usado
## Estrutura do projeto
![image](https://github.com/SrJohn369/Scripts-Dados-Loteria/assets/106630200/1c786a2a-05f9-4ee3-8a3e-cc0d0c6270af)
## Requisitos e Execução
Para que este repositório seja executado em sua máquina alguns requisitos devem ser atendidos.
* Faça o download do repositório clicando [aqui](https://github.com/SrJohn369/Scripts-Dados-Loteria/archive/refs/heads/main.zip).
* Você deve ter instalado no seu sistema `Python v3.11`+.
* Crie um Ambiente virtual na pasta com o comando: ```python -m venv nome-do-ambiente``` (Modifique o `.gitignore` adcionando seu ambiente criado).
* Ative seu ambiente virtual e execute o arquivo requirements.txt com o comando ```pip install -r requirements.txt``` para instalar os requisitos necessários.
* Faça uma concexão com seu banco. Dependendo de sua necessidade é possível fazer uma conexão local, e aqui neste reposito há um exemplo desta conexão local usando `pycopg2` para fazer conexão com PostgreSQL `./connections/sqliteTestDB.py`. Caso deseje uma conexão com um banco de dados remoto como Supabase para projetos de site e etc. é recomendado usar uma ORM como `SQLAlchemy`.
* Por fim, uma boa prática também é criar um arquivo `.env` ponha todas suas variáveis de conexão lá e para garantir que as variaveis vão ser detectadas use o modulo python-dotenv que pode pode ser baixado pelo comando `pip install python-dotenv`.
#### func_SQLITE.py  
Para executar tanto este script quanto os outros basta usar o arquivo main.py para chamar as funções principais como no exemplo a seguir:  
  
![image](https://github.com/SrJohn369/Scripts-Dados-Loteria/assets/106630200/40ab1f10-0c65-45d7-af24-f991714047c5)  
Então no seu terminal use `py main.py` para executar o arquivo e adicionar os dados  
#### func_PSQL_Alchemy.py
A execução deste é a mesma do `func_SQLITE.py` porém os arquivos tem suas diferenças:  
![image](https://github.com/SrJohn369/Scripts-Dados-Loteria/assets/106630200/e63b3193-5cf4-43f4-8ee3-c14aa92ba8dd)  
Na função `adicionar_dados()` em `lotoFaciel()` possui um atributo `Jogo` que deverá receber uma classe do arquivo models.py que conterá os modelos para criar as tabelas no banco de dados.  
Na mesma função `adicionar_dados()`, agora em `sqliteTestDB()` o atributo é `tabela` que receberá apenas um nome para a tabela que irá ser criada  
## Contribuidores
|[<img src="https://github.com/SrJohn369.png" width="100" height="100"><br><sub>João Victor</sub>](https://github.com/SrJohn369)|
| :---: |
