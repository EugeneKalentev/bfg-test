from pyramid.security import Allow, Everyone

import datetime

from sqlalchemy import (
    Column,
    Integer,
    Text,
    Unicode,
    UnicodeText,
    DateTime,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(
    sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Page(Base):
    __tablename__ = 'wikipages'
    uid = Column(Integer, primary_key=True)
    title = Column(Text, unique=True)
    body = Column(Text)

class AllResults(Base):
    __tablename__ = 'allresults'
    id = Column(Integer, primary_key=True)
    dt = Column(DateTime, default=datetime.datetime.now)
    title = Column(UnicodeText)
    name = Column(UnicodeText)
    link = Column(UnicodeText)

class Search(Base):
    __tablename__ = 'search'
    id = Column(Integer, primary_key=True)
    dt = Column(DateTime, default=datetime.datetime.now)
    title = Column(UnicodeText)
    name = Column(UnicodeText)




class Root(object):
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, 'group:editors', 'edit')]

    def __init__(self, request):
        pass