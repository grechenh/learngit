from datetime import datetime
from decimal import Decimal
from typing import Annotated, Optional

from sqlalchemy import String, Text, Enum, Numeric, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

id_pk = Annotated[int, mapped_column(primary_key=True, autoincrement=True, comment='pk_id')]
# create_datetime = Annotated[datetime, mapped_column(nullable=False, default=datetime.now, comment='type datetime')]


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = 'os_category'
    id: Mapped[id_pk]
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, comment='Category_name')

    movies: Mapped[list['Movie']] = relationship(
        'Movie',
        back_populates='category',
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Category id={self.id} name={self.name}>"


class Movie(Base):
    __tablename__ = 'os_movie'
    id: Mapped[id_pk]
    title: Mapped[str] = mapped_column(String(100), nullable=False, default='no title', comment='Movie_title')
    mins: Mapped[int] = mapped_column(nullable=False, default=0, comment='mins=')
    summary: Mapped[str] = mapped_column(Text, nullable=False, default='no summary', comment='summary')
    release_date: Mapped[Optional[datetime]] = mapped_column(nullable=True, default=None, comment='电影上映日期')

    category_id: Mapped[int] = mapped_column(
        ForeignKey(
            'os_category.id',
            ondelete='CASCADE',
            name='fk_movie_category_id'
        ),
        nullable=False,
        index=True,
        comment='fk_movie_category_id'
    )

    category: Mapped['Category'] = relationship(
        'Category',
        back_populates='movies',
        passive_deletes=True,
        lazy='joined'
    )

    movieActors: Mapped[list['MovieActor']] = relationship(
        'MovieActor',
        back_populates='movie',
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f"<Movie id={self.id} title={self.title} mins={self.mins} summary={self.summary} release_date={self.release_date} category_id={self.category_id}>"


class Actor(Base):
    __tablename__ = 'os_actor'
    id: Mapped[id_pk]
    name: Mapped[str] = mapped_column(String(100), nullable=False, comment='Actor_name')
    nickname: Mapped[str] = mapped_column(String(100), nullable=False, comment='Nickname')
    gender: Mapped[str] = mapped_column(Enum('男','女'), nullable=False, comment='Actor_gender')

    profile: Mapped[Optional['Profile']] = relationship(
        'Profile',
        back_populates='actor',
        uselist=False,
        cascade='all, delete-orphan'
    )

    movieActors: Mapped[list['MovieActor']] = relationship(
        'MovieActor',
        back_populates='actor',
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f"<Actor id={self.id}  name={self.name}  nickname={self.nickname} gender={self.gender}>"


class Profile(Base):
    __tablename__ = 'os_profile'
    id: Mapped[id_pk]
    constellation: Mapped[str] = mapped_column(Enum('射手座','水瓶座','金牛座','狮子座'), nullable=False, comment='four constellation')
    blood_type: Mapped[str] = mapped_column(Enum('A','B','AB','O'), nullable=False, comment='blood_type')
    height: Mapped[int] = mapped_column(nullable=False, comment='height(cm)')
    weight: Mapped[Decimal] = mapped_column(Numeric(precision=5, scale=2), nullable=False, comment='max= 999.99 kg')

    actor_id: Mapped[int] = mapped_column(
        ForeignKey(
            'os_actor.id',
            name='fk_profile_actor_id',
            ondelete='CASCADE'
        ),
        nullable=False,
        unique=True,
        index=True,
        comment='fk_profile_actor_id'
    )

    actor: Mapped['Actor'] = relationship(
        'Actor',
        back_populates='profile',
        passive_deletes=True,
        lazy='joined'
    )

    def __repr__(self):
        return f"<Profile id={self.id}  constellation={self.constellation}  blood_type={self.blood_type} height={self.height} weight={self.weight} actor_id={self.actor_id}>"


class MovieActor(Base):
    __tablename__ = 'os_movieActor'
    movie_id: Mapped[int] = mapped_column(
        ForeignKey(
            'os_movie.id',
            name='fk_movieActor_movie_id',
            ondelete='CASCADE',
            onupdate='CASCADE'
        ),
        primary_key=True,
        nullable=False,
        comment='一个电影对应多位主演记录'
    )

    movie: Mapped['Movie'] = relationship(
        'Movie',
        back_populates='movieActors',
        passive_deletes=True,
        lazy='joined'
    )

    actor_id: Mapped[int] = mapped_column(
        ForeignKey(
            'os_actor.id',
            name='fk_movieActor_actor_id',
            ondelete='CASCADE',
            onupdate='CASCADE'
        ),
        primary_key=True,
        nullable=False,
        comment='一位演员对应多位主演记录'
    )

    actor: Mapped['Actor'] = relationship(
        'Actor',
        back_populates='movieActors',
        passive_deletes=True,
        lazy='joined'
    )

    def __repr__(self):
        return f"<MovieActor movie_id={self.movie_id}  actor_id={self.actor_id}>"
