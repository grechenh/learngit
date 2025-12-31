from datetime import datetime
from typing import Annotated

from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import Integer, String, Enum

int_pk = Annotated[int, mapped_column(Integer, primary_key= True, autoincrement= True, nullable= False, comment='编号')]
name = Annotated[str, mapped_column(String(32), nullable= False, comment='姓名')]
create_time = Annotated[datetime, mapped_column(datetime, default=datetime.now(),nullable= False, comment='创建时间')]


class Base(DeclarativeBase):
    pass


class Department(Base):
    __tablename__ = 'departments'

    id: Mapped[int_pk]
    name:Mapped[name] = mapped_column(comment='部门名称')


class Emplonee(Base):
    id: Mapped[int_pk]
    name: Mapped[name] = mapped_column(comment='员工名称')
    gender: Mapped[Enum] = mapped_column(Enum('男','女'),nullable= False, comment='性别')
    phone:Mapped[str] = mapped_column(String(11), unique= True, comment='phone')
    create_at: Mapped[create_time]