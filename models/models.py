from sqlalchemy import Column, Integer, String, Date

from connections.connect_SQLAlchemy import Base, criar_db


class Milionaria(Base):

    __tablename__ = "milionaria"

    concurso = Column(Integer, primary_key=True)
    data_sorteio = Column(Date)
    bola1 = Column(Integer)
    bola2 = Column(Integer)
    bola3 = Column(Integer)
    bola4 = Column(Integer)
    bola5 = Column(Integer)
    bola6 = Column(Integer)
    trevo1 = Column(Integer)
    trevo2 = Column(Integer)


class Quina(Base):
    
    __tablename__ = "quina"
    
    concurso = Column(Integer, primary_key=True)
    data_sorteio = Column(Date)
    bola1 = Column(Integer)
    bola2 = Column(Integer)
    bola3 = Column(Integer)
    bola4 = Column(Integer)
    bola5 = Column(Integer)
    
    
class LotoFacil(Base):
    
    __tablename__ = "lotofacil"
    
    concurso = Column(Integer, primary_key=True)
    data_sorteio = Column(Date)
    bola1 = Column(Integer)
    bola2 = Column(Integer)
    bola3 = Column(Integer)
    bola4 = Column(Integer)
    bola5 = Column(Integer)
    bola6 = Column(Integer)
    bola7 = Column(Integer)
    bola8 = Column(Integer)
    bola9 = Column(Integer)
    bola10 = Column(Integer)
    bola11 = Column(Integer)
    bola12 = Column(Integer)
    bola13 = Column(Integer)
    bola14 = Column(Integer)
    bola15 = Column(Integer)
    
    
class MegaSena(Base):
     
    __tablename__ = "megasena"
    
    concurso = Column(Integer, primary_key=True)
    data_do_sorteio = Column(Date)
    bola1 = Column(Integer)
    bola2 = Column(Integer)
    bola3 = Column(Integer)
    bola4 = Column(Integer)
    bola5 = Column(Integer)
    bola6 = Column(Integer)
    
    
criar_db()
print("!!--TABELA CRIADA--!!")