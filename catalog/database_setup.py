from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

Base = declarative_base()

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'catalog',
    'password': 'catalog',
    'database': 'catalog'
}


class User(Base):
    __tablename__ = 'userdb'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    items = relationship("Item", back_populates="category", cascade="all, delete-orphan")

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
               'id': self.id,
               'name': self.name,
               'items': [i.serialize for i in self.items]
        }


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(Text, nullable=False)
    pic_name = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship("Category", back_populates="items")
    user_id = Column(Integer, ForeignKey('userdb.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
               'category_name': self.category.name,
               'description': self.description,
               'title': self.name,
               'id': self.id,
               'user_id': self.user_id
        }


engine = create_engine(URL(**DATABASE))
Base.metadata.create_all(engine)
