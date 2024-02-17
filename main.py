from funcs.func_PSQL_Alchemy import criar_dataFrame, adicionar_dados
from models.models import *


def milionaria():
    dataFrame = criar_dataFrame("./data/+Milionária.xlsx", 10)
    adicionar_dados(dataFrame, Jogo=Milionaria)


def quina():
    dataFrame = criar_dataFrame("./data/Quina.xlsx", 7)
    adicionar_dados(dataFrame, Jogo=Quina)
    

def megaSena():
    dataFrame = criar_dataFrame("./data/Mega-Sena.xlsx", 8)
    adicionar_dados(dataFrame, Jogo=MegaSena)
    
def lotoFacil():
    dataFrame = criar_dataFrame("./data/Lotofácil.xlsx", 17)
    adicionar_dados(dataFrame, Jogo=LotoFacil)


if __name__ == "__main__":
    lotoFacil()