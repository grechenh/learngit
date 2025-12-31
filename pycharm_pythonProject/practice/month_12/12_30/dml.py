from sqlalchemy.orm import sessionmaker, aliased

from models import Base, Category, Article
from sqlalchemy import create_engine, select

engine = create_engine('mysql+mysqldb://root:root@127.0.0.1/homework', echo=True)

Session = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def create_table():
    Base.metadata.create_all(engine)


def insert_data():
    with Session() as db_session:
        # 创建分类
        programming = Category(
            name="编程技术",
            description="关于编程语言、框架、工具等技术文章"
        )

        lifestyle = Category(
            name="生活随笔",
            description="日常生活感悟、读书笔记等"
        )

        # 创建文章
        articles = [
            Article(
                title="Python异步编程入门",
                content="本文将介绍Python中的async/await语法...",
                category=programming
            ),
            Article(
                title="SQLAlchemy 2.0新特性详解",
                content="SQLAlchemy 2.0带来了许多重要的变化...",
                category=programming
            ),
            Article(
                title="我的阅读习惯养成记",
                content="如何养成每天阅读的习惯...",
                category=lifestyle
            ),
            Article(
                title="周末咖啡时光",
                content="周末的早晨，一杯咖啡，一本好书...",
                category=lifestyle
            ),
            Article(
                title="深入理解FastAPI",
                content="FastAPI是一个现代、快速的Python Web框架...",
                category=programming
            )
        ]

        # 添加到session并提交
        db_session.add(programming)
        db_session.add(lifestyle)
        db_session.add_all(articles)
        db_session.commit()


def select_from_article_id(article_id: int):
    with Session() as select_session:
        a = aliased(Article)
        statement = select(a).where(a.id == article_id)
        print(f'statement={statement}')
        result = select_session.execute(statement).scalar_one_or_none()
        print(f'result={result}')
        # scalar_result = result
        # print(f'scalar_result={scalar_result}')


if __name__ == '__main__':
    # create_table()
    # insert_data()
    select_from_article_id(1)
    pass
