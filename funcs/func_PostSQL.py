from connections.connect_DB_PSQL import *


conn = conectarBanco()


def criar_dataFrame(arquivoXLSX: str, qntd_colunm: int) -> dict:
    '''
    arquivoXLSX - Este arquivo deve ser do tipo .xlsx \n
    qntd_colunm - quantidade de colunas para o novo DataFrame \n
    esta função irá capturar todos os dados do arquivo .xlsx e criará um dicionário 
    com todos os dados.
    '''
    import pandas as pd

    df = pd.read_excel(arquivoXLSX)
    novo_df = {}

    for i, chaves in enumerate(df.keys()):
        if i < qntd_colunm:
            chaves_old = chaves
            chaves = str(chaves)
            chaves = chaves.replace('+', '').lower()
            chaves = chaves.replace(' ', '_').lower()
            chaves = chaves.replace('/', '_').lower()
            novo_df[chaves] = df[chaves_old]

    return novo_df


def adicionar_dados(dataFrame: dict, tabela: str):
    '''
    dataFrame - Deverá receber um dicionário com os dados capturados do xlsx. \n
    conn - conexão com banco e dados. \n
    tabela - Nome da tabela que irá ser criada. \n
    Esta função deverá criar tabelas caso não exista e armazenar os dados nesta tabela. 
    A função irá dar dados de status de cada coluna adicionada
    '''

    cursor = conn.cursor()

    ####### CRIAR TABELA #######
    try:
        table = f'CREATE TABLE IF NOT EXISTS {tabela} '
        for i, column in enumerate(dataFrame.keys()):
            if i == 0:
                table += f'({column} PRIMARY KEY,'
            elif len(dataFrame.keys()) == (i+1):
                table += f'{column} SMALLINT);'
            else:
                if column == 'data_sorteio':
                    table += f'{column} DATE, '
                else:
                    table += f'{column} SMALLINT, '
        
        input(f'!!! ---- TABELA CRIADA COM SUCESSO (caso não exista)---- !!!\
              \n{table}\n APERTE ENTER PARA SALVAR E CONTINUAR...')
        cursor.execute(table)
        conn.commit()

    except psycopg2.Error as err:
        return "Erro ao criar a tabela: ", err

    ######## ADICIONAR DADOS À TABELA ########
    try: 

        print("...Adicionando dados...")

        # Utizamos concurso pois é imutável e referece tanto ao sorteio quanto a data dele 
        # e cada linha representa um sorteio diferente
        for line in range(len(dataFrame['concurso'])):
            # Vamo criar uma query para gerar um SQL
            query = f'INSERT INTO {tabela} VALUES ('

            values = []
            
            # adiciona dados de acordo com a linha
            for column in dataFrame.keys():
                values.append(dataFrame[column][line])

            # iterar string para adicionar os dados de forma dinânmica para evitar error de integridade de dados
            for i, value in enumerate(values):
                if i == 1:
                    query += f"TO_DATE('{value}', 'DD-MM-YYYY'), "
                elif (i+1) == len(values):
                    query += f"{value});"
                else:
                    query += f"{value}, "
            
            # DEBUG
            print("VALOR ADICIONADO: \n",query)
            cursor.execute(query)


        print("!!OS DADOS AINDA NÃO FORAM SALVOS!!")
        input("OS DADOS SERÃO SALVOS APERTE ENTER PARA CONFIRMAR...")
        conn.commit()        
        print("DADOS SALVOS COM SUCESSO!!")

    except psycopg2.Error as err:
        conn.rollback()
        return "Erro ao adicionar dados: ", err


if __name__ == "__main__":
    pass