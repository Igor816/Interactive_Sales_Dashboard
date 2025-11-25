from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, Numeric


class Base(DeclarativeBase):
	pass



class Sale(Base):
    __tablename__  = 'sales'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()
    total_amount: Mapped[int] = mapped_column()
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    region_id: Mapped[int] = mapped_column(ForeignKey('regions.id'))
    product: Mapped[int] = relationship("Product")
    region: Mapped[int] = relationship("Region")
    
class Product(Base):
    __tablename__  = 'products'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    price: Mapped[Numeric] = mapped_column()
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    category = relationship("Category")
    
class Categorie(Base):
    __tablename__  = 'categories'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    

class Region(Base):
    __tablename__  = 'regions'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
 
 

