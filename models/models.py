from sqlalchemy import Column, Integer, String

from connections.connect_SQLAlchemy import Base


class Milionaria(Base):

    __tablename__ = "milionaria"

    concurso = Column(Integer, primary_key=True)
    data_sorteio = Column(String)
    bola1 = Column(Integer)
    bola2 = Column(Integer)
    bola3 = Column(Integer)
    bola4 = Column(Integer)
    bola5 = Column(Integer)
    bola6 = Column(Integer)
    trevo1 = Column(Integer)
    trevo2 = Column(Integer)
