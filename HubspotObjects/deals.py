from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer
from HubspotObjects.SQLAlchemy import Base

class Deals(Base):

    # Table name
    __tablename__ = 'deals'

    # Table columns
    id = Column(Integer(), primary_key=True)
    dealname = Column(String(), unique=True, nullable=False)

    def __repr__(self):
        return f"dealname={self.dealname}"
