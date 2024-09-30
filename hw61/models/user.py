from app.backend.db import Base
from sqlalchemy import Integer, PrimaryKeyConstraint, String, Boolean, ForeignKey, Column, null
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship('task', back_populates='user')
