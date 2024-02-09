# from connect_DB import conectarBanco


import pandas as pd
import sqlite3 as sql


def principal():
    cria_conecta_insere()


def cria_conecta_insere():
    conn = sql.connect("resultLOTOFACIL.db")
    cursor = conn.cursor()

    df = pd.read_excel("./xlsx/Lotofácil.xlsx")
    novo_df = {}

    for chaves in df.keys():
        chaves_old = chaves
        chaves = str(chaves)
        chaves = chaves.replace('+', '').lower()
        chaves = chaves.replace(' ', '_').lower()
        novo_df[chaves] = df[chaves_old]

    table = 'CREATE TABLE IF NOT EXISTS resultado '
    for i, key in enumerate(novo_df.keys()):
        if i == 0:
            table += f'({key} PRIMAY KEY,'
        elif len(novo_df.keys()) == (i+1):
            table += f'{key});'
        else:
            table += f'{key}, '

    cursor.execute(table)
    print("Tabela criada com sucesso!")
    
    
    print("...Adicionando dados...")
    for j, key in enumerate(novo_df.keys()):
        print("Coluna a adicionar:", key)
        input("Enter para continuar...")
        for k, valor in enumerate(novo_df[key]):
            if j == 0:
                cursor.execute(
                    f"""INSERT INTO resultado ({key}) VALUES ({valor});"""
                )
                print("Status:", f"{k+1}" + " /", len(novo_df[key]))
            elif j > 0:
                #Em -> WHERE concurso = '{novo_df["concurso"][k]}'; é feito assim para evitar erros de contagem por exemplo 2894 e logo após 2896 que quebra a contagem  
                cursor.execute(
                    f"""UPDATE resultado
                        SET {key} = '{valor}'
                        WHERE concurso = '{novo_df["concurso"][k]}';"""
                )
                print("Status:", f"{k+1}" + " /", len(novo_df[key]))
        conn.commit()
        print("\nAdicionado:", "Status:", f"{j+1} /", len(novo_df.keys()))
        input("Enter para continuar...")
        

    conn.close()


if __name__ == '__main__':
    principal()
