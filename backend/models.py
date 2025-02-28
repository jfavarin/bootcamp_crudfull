from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy import func
from database import Base

class ProductModel(Base):
    __tablename__ = "product" #vai ser o nome da minha tabela

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    categoria = Column(String, index=True)
    email_fornecedor = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), default=func.now(), index=True)


