from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

from database import Base


class ContactModel(Base):
    __tablename__ = 'Contacts'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), primary_key=False, nullable=False)
    phone = Column(String(20), primary_key=False, nullable=False)
    email = Column(String(255), primary_key=False, nullable=True)
    adrress = Column(String(200), primary_key=False, nullable=True)
    notes = Column(Text, primary_key=False, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))