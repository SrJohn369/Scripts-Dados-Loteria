import psycopg2
import os


# Defina as informações de conexão
dbname = os.environ("DB_NAME")
user = os.environ("USER")
password = os.environ("PASSWORD")
host = os.environ("HOST")
port = os.environ("PORT")


# Conecte-se ao banco de dados
def conectarBanco():
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

        print("Conexão bem-sucedida!")

        return conn

    except psycopg2.Error as err:
        print("Erro ao conectar ao banco de dados: ", err)


if __name__ == "__main__":
    pass