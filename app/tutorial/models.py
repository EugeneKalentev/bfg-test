from pyramid.security import Allow, Everyone
import re
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

def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', str(s))

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
    slug = Column(UnicodeText)

    def __init__(self, *args, **kwargs):
        super(AllResults, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<AllResults id: {}, title: {}>'.format(self.id, self.title)

class Search(Base):
    __tablename__ = 'search'
    id = Column(Integer, primary_key=True)
    dt = Column(DateTime, default=datetime.datetime.now)
    title = Column(UnicodeText)
    name = Column(UnicodeText)
    label = Column(UnicodeText)

class Root(object):
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, 'group:editors', 'edit')]

    def __init__(self, request):
        pass