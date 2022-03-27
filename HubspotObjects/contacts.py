from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer
from HubspotObjects.SQLAlchemy import Base

class Contacts(Base):

    # Table name
    __tablename__ = 'contacts'

    # Table columns
    __tablename__ = 'contacts'
    id = Column(Integer(), primary_key=True)
    username = Column(String(25), unique=True, nullable=False)

    def __repr__(self):
        return f"username={self.username}"
