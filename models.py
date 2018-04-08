# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Index, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from Cache import engine

Base = declarative_base()
metadata = Base.metadata


class Billboard(Base):
    __tablename__ = 'billboard'
    __table_args__ = (
        Index('rank', 'rank', 'date'),
    )

    def __init__(self, previous, weeks, peak, rank, date):
        self.previous = previous
        self.weeks = weeks
        self.peak = peak
        self.rank = rank
        self.date = date


    previous = Column(Integer)
    weeks = Column(Integer)
    peak = Column(Integer)
    rank = Column(Integer, primary_key=True, nullable=False)
    date = Column(DateTime, primary_key=True, nullable=False)


class Singer(Base):
    __tablename__ = 'singer'

    url = Column(String(255), primary_key=True)
    id = Column(Integer)
    image = Column(String(255))
    name = Column(String(255))
    info = Column(Text)
    area = Column(String(255))
    type = Column(String(255))
    born = Column(Date)


class Song(Base):
    __tablename__ = 'song'

    def __init__(self, id, title):
        self.id = id
        self.title = title

    id = Column(Integer, primary_key=True)
    title = Column(String(255))


class Songonbillboard(Base):
    __tablename__ = 'songonbillboard'
    __table_args__ = (
        Index('billboardRank', 'billboardRank', 'billboardDate'),
    )

    id = Column(Integer, primary_key=True)
    songId = Column(Integer, index=True)
    billboardDate = Column(DateTime)
    billboardRank = Column(Integer)


class Songtosinger(Base):
    __tablename__ = 'songtosinger'

    def __init__(self, songId, singerName):
        self.songId = songId
        self.singerName = singerName

    id = Column(Integer, primary_key=True)
    songId = Column(Integer, index=True)
    singerName = Column(String(255), index=True)

    # Base.metadata.create_all(engine)
