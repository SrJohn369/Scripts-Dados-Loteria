from funcs.func_PSQL_Alchemy import criar_dataFrame, adicionar_dados
from models.models import Milionaria


def milionaria():
    dataFrame = criar_dataFrame("./data/+Milionária.xlsx", 10)
    adicionar_dados(dataFrame, Jogo=Milionaria)


if __name__ == "__main__":
    milionaria()