from app.backend.db import Base
from sqlalchemy import Integer, PrimaryKeyConstraint, String, Boolean, ForeignKey, Column, null
from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index= True)
    slug = Column(String, unique=True, index=True)
    user = relationship('user', back_populates='task')
