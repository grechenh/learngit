from decimal import Decimal
from fastapi import HTTPException
from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from sqlalchemy import String, Numeric
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Library(Base):
    __tablename__ = 'os_library'
    id: Mapped[int] = mapped_column(primary_key=True, comment='唯一标识')
    title: Mapped[str] = mapped_column(String(32), nullable=False, comment='书名（必填）')
    year: Mapped[int] = mapped_column(nullable=False, comment='出版年份')
    isbn: Mapped[Optional[str]] = mapped_column(String(32), nullable=True, comment='ISBN号（可选）')
    price: Mapped[Decimal] = mapped_column(Numeric(precision=5, scale=2), nullable=False, comment='价格')

    def __repr__(self):
        return f"<Library id={self.id} title={self.title} year={self.year} isbn={self.isbn} price={self.price}>"


library1 = Library(id=1, title='Python入门', year=2020, isbn='1234567890', price=Decimal('99.99'))
library2 = Library(id=2, title='Java入门', year=2019, isbn='0987654321', price=Decimal('89.99'))
library3 = Library(id=3, title='C++入门', year=2021, isbn='1122334455', price=Decimal('79.99'))
library4 = Library(id=4, title='C#入门', year=2022, isbn='5566778899', price=Decimal('69.99'))
library5 = Library(id=5, title='Go入门', year=2022, isbn='9988776655', price=Decimal('59.99'))

cont = [library1, library2, library3, library4, library5]



class BookOut(BaseModel):
    id: int
    title: str
    year: int
    isbn: Optional[str]
    price: float  # 前端友好

    model_config = ConfigDict(from_attributes=True)




app = FastAPI()


@app.get("/", response_model=List[BookOut])
def home():
    return cont
    pass


@app.get("/books", response_model=List[BookOut])
def books(year: int = None):
    if year:
        return [book for book in cont if book.year == year]  # 返回列表
    else:
        return cont


@app.get("/books/{books_id}", response_model=BookOut)
def books_id(books_id: int):
    for book in cont:
        if book.id == books_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8088,
        reload=True,
        log_level="info"
    )

    pass