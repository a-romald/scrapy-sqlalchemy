from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()

class AllData(DeclarativeBase):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(2000))
    price = Column(String(20))
    image = Column(String(255))
    imageurl = Column(String(255))

    def __init__(self, id=None, title=None, description=None, price=None, image=None, imageurl=None):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.image = image
        self.imageurl = imageurl

    def __repr__(self):
        return "<AllData: id='%d', title='%s', description='%s', price='%s', image='%s', imageurl='%s'>" % (self.id, self.title, self.description, self.price, self.image, self.imageurl)
