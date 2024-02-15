import psycopg2
import os


# Defina as informações de conexão
__dbname = os.environ.get("DB_NAME")
__user = os.environ.get("USER")
__password = os.environ.get("PASSWORD")
__host = os.environ.get("HOST")
__port = os.environ.get("PORT")


# Conecte-se ao banco de dados
def conectarBanco():
    try:
        conn = psycopg2.connect(
            dbname=__dbname,
            user=__user,
            password=__password,
            host=__host,
            port=__port
        )

        print("Conexão bem-sucedida!")

        return conn

    except psycopg2.Error as err:
        print("Erro ao conectar ao banco de dados: ", err)


if __name__ == "__main__":
    pass