from  types import list, Optional  
from pytest import Item
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import  DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    # table name users 
    __tablename__ = "users"

    # columns 
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[Optional[str]] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    items: Mapped[list["Item"]] = relationship(back_populates="owner")
    
    # A helper method to make printing objects nicer
    def  __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, email={self.email})"
    