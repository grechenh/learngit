from datetime import datetime
from typing import Annotated

from sqlalchemy import DateTime, Text, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, mapped_column, Mapped, relationship

id_pk = Annotated[int, mapped_column(primary_key=True, autoincrement=True, nullable=False, comment='主键编号')]
create_at = Annotated[datetime, mapped_column(DateTime, default=datetime.now, comment='创建时间')]

Base = declarative_base()


class Category(Base):
    __tablename__ = 'os_category'
    id: Mapped[id_pk]
    name: Mapped[str] = mapped_column(String(32), nullable=False, unique=True, default='no name', comment='must')
    description: Mapped[str] = mapped_column(Text, nullable=False, default='no description', comment='description')
    create_at: Mapped[create_at]

    articles: Mapped[list['Article']] = relationship(
        'Article',
        back_populates='category',
        # lazy='selectin',
        cascade='all, delete-orphan'
    )
    pass

    def __repr__(self):
        return f'<Category(id={self.id}, name="{self.name}", description="{self.description}")>'


class Article(Base):
    __tablename__ = 'os_article'
    id: Mapped[id_pk]
    title: Mapped[str] = mapped_column(String(100), nullable=False, default='no title', comment='标题')
    content: Mapped[str] = mapped_column(Text, nullable=False, default='no content', comment='内容')
    create_at: Mapped[create_at]
    update_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')

    category_id: Mapped[int] = mapped_column(
        ForeignKey('os_category.id',
                   ondelete="CASCADE",
                   name='fk_article_category_id'
                   ),
        nullable=False,
        index=True,
        comment='category id'
    )

    # 子类关联
    category: Mapped[Category] = relationship(
        'Category',
        back_populates='articles',
        passive_deletes=True,
        lazy='joined',
    )

    def __repr__(self):
        return f"<article(id={self.id}, title='{self.title}', content='{self.content}', update_at='{self.update_at}')>"
