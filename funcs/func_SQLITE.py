# "./xlsx/Lotofácil.xlsx"


def criar_novo_df(arquivoXLSX: str, qntd_colunm: int) -> dict:
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
    import sqlite3 as sql

    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    ####### CRIAR TABELA #######
    try:
        table = f'CREATE TABLE IF NOT EXISTS {tabela} '
        for i, key in enumerate(dataFrame.keys()):
            if i == 0:
                table += f'({key} SERIAL PRIMARY KEY,'
            elif len(dataFrame.keys()) == (i+1):
                table += f'{key} SMALLINT);'
            else:
                if key == 'data_sorteio':
                    table += f'{key} DATE, '
                else:
                    table += f'{key} SMALLINT, '
        
        cursor.execute(table); print(table)

    except sql.Error as err:
        return "Erro ao criar a tabela: ", err

    ######## ADICIONAR DADOS À TABELA ########
    try: 

        print("...Adicionando dados...")
        for j, key in enumerate(dataFrame.keys()):
            print("Coluna a adicionar:", key)
            input(f"Inciando o insert da coluna {key}...Enter para continuar...")
            for k, valor in enumerate(dataFrame[key]):
                if j == 0:
                    cursor.execute(
                        f"""INSERT INTO {tabela} ({key}) VALUES ({valor});"""
                    )
                    print("Status:", f"{k+1}" + " /", len(dataFrame[key]))
                elif j > 0:
                    #Em -> WHERE concurso = '{dataFrame["concurso"][k]}'; é feito assim para evitar erros de contagem por exemplo 2894 e logo após 2896 que quebra a contagem  
                    cursor.execute(
                        f"""UPDATE {tabela}
                            SET {key} = '{valor}'
                            WHERE concurso = '{dataFrame["concurso"][k]}';"""
                    )
                    print("Status:", f"{k+1}" + " /", len(dataFrame[key]))
            
            print("\nAdicionado:", "Status:", f"{j+1} /", len(dataFrame.keys()))
            print("!!OS DADOS AINDA NÃO FORAM SALVOS!!")
            input("Enter para continuar para próxima coluna...")
        input("OS DADOS SERÃO SALVOS APERTE ENTER PARA CONFIRMAR...")
        conn.commit()
        conn.close()

    except sql.Error as err:
        conn.rollback()
        return "Erro ao adicionar dados: ", err


novo_df = criar_novo_df("./xlsx/Lotofácil.xlsx", 17)

# query += "('" + "', '".join(str(value) for value in values) + "');"