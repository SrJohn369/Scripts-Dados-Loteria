from connections.connect_SQLAlchemy import get_db
from datetime import datetime

import numpy as np
import os
import traceback


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


def adicionar_dados(dataFrame: dict, Jogo: any):
    '''
    dataFrame - Deverá receber um dicionário com os dados capturados do xlsx. \n
    conn - conexão com banco e dados. \n
    tabela - Nome da tabela que irá ser criada. \n
    Esta função deverá criar tabelas caso não exista e armazenar os dados nesta tabela. 
    A função irá dar dados de status de cada coluna adicionada
    '''
    ######## ADICIONAR DADOS À TABELA ########
    with get_db() as db:
        try: 
            print("\n!!Conexão bem sucedida!!\n")
            input("Aperte ENTER para continuar...")
            print("...Adicionando dados...")

            # Utizamos concurso pois é imutável e referece tanto ao sorteio quanto a data dele 
            # e cada linha representa um sorteio diferente
            for line in range(len(dataFrame['concurso'])):

                values = {}
                
                # adiciona dados de acordo com a linha
                for column in dataFrame.keys():
                    # Convertendo valores numpy.int64 para int
                    if isinstance(dataFrame[column][line], np.int64):
                        values[column] = int(dataFrame[column][line])
                    else:
                        # Convertendo valores str para formato timestamp para Date para o DB
                        data = dataFrame[column][line]
                        data_foramatada = datetime.strptime(data, "%d/%m/%Y")
                        values[column] = data_foramatada

                # Adicioando dados
                data_concurso = Jogo(**values)
                db.add(data_concurso)
                
                # DEBUG
                os.system("cls")
                print(f"(Status)Concurso adicionado: {line+1} / {len(dataFrame['concurso'])}")

            print("!!OS DADOS AINDA NÃO FORAM SALVOS!!")
            input("OS DADOS SERÃO SALVOS APERTE ENTER PARA CONFIRMAR...")
            
            db.commit()
            
            print("DADOS SALVOS COM SUCESSO!!")

        except Exception as e:
            db.rollback()
            print("Erro ao adicionar dados:", e)
            print(traceback.format_exc())


if __name__ == "__main__":
    pass