from datetime import datetime
from decimal import Decimal

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from models import Base, Category, Actor, Profile, MovieActor, Movie

engine = create_engine('mysql+mysqldb://root:root@127.0.0.1/homework1', echo=True)

Session = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def crete_table():
    Base.metadata.create_all(engine)


def insert_test():
    with Session() as session:
        try:
            categories = [
                Category(name="动作片"),
                Category(name="喜剧片"),
                Category(name="爱情片"),
                Category(name="科幻片"),
                Category(name="恐怖片"),
            ]
            session.add_all(categories)
            session.flush()
            print(f"创建了 {len(categories)} 部电影分类")

            actors = [
                Actor(name="张艺谋", nickname="老谋子", gender="男"),
                Actor(name="吴京", nickname="战狼", gender="男"),
                Actor(name="章子怡", nickname="国际章", gender="女"),
                Actor(name="沈腾", nickname="沈叔叔", gender="男"),
                Actor(name="周冬雨", nickname="冬叔", gender="女"),
                Actor(name="黄渤", nickname="青岛贵妇", gender="男")
            ]
            session.add_all(actors)
            session.flush()
            print(f"创建了 {len(actors)} 个演员")

            profiles = [
                Profile(actor_id=actors[0].id, constellation="射手座", blood_type="A", height=165,
                        weight=Decimal("60.50")),
                Profile(actor_id=actors[1].id, constellation="金牛座", blood_type="O", height=175,
                        weight=Decimal("70.20")),
                Profile(actor_id=actors[2].id, constellation="水瓶座", blood_type="B", height=164,
                        weight=Decimal("48.80")),
                Profile(actor_id=actors[3].id, constellation="射手座", blood_type="A", height=180,
                        weight=Decimal("75.30")),
                Profile(actor_id=actors[4].id, constellation="狮子座", blood_type="AB", height=162,
                        weight=Decimal("44.50")),
            ]
            session.add_all(profiles)
            session.flush()
            print(f"创建了 {len(profiles)} 个演员详情")

            movies = [
                Movie(
                    title="战狼2",
                    mins=123,
                    summary="讲述脱下军装的冷锋被卷入了一场非洲国家的叛乱，本来能够安全撤离的他无法忘记军人的职责，重回战场展开救援的故事。",
                    release_date=datetime(2017, 7, 27),
                    category_id=categories[0].id
                ),
                Movie(
                    title="你好，李焕英",
                    mins=128,
                    summary="2001年的某一天，刚刚考上大学的贾晓玲经历了人生中的一次大起大落。一心想要成为母亲骄傲的她却因母亲突遭严重意外，而悲痛万分。",
                    release_date=datetime(2021, 2, 12),
                    category_id=categories[1].id
                ),
                Movie(
                    title="流浪地球",
                    mins=125,
                    summary="太阳即将毁灭，人类在地球表面建造出巨大的推进器，寻找新家园。然而宇宙之路危机四伏，为了拯救地球，流浪地球时代的年轻人挺身而出，展开争分夺秒的生死之战。",
                    release_date=datetime(2019, 2, 5),
                    category_id=categories[3].id
                ),
                Movie(
                    title="少年的你",
                    mins=135,
                    summary="一场高考前夕的校园意外，改变了两个少年的命运。陈念性格内向，是学校里的优等生，努力复习、考上好大学是她高三唯一的念头。",
                    release_date=datetime(2019, 10, 25),
                    category_id=categories[2].id
                ),
                Movie(
                    title="我和我的祖国",
                    mins=155,
                    summary="该片讲述了新中国成立70年间普通百姓与共和国息息相关的故事。",
                    release_date=datetime(2019, 9, 30),
                    category_id=categories[0].id
                )
            ]
            session.add_all(movies)
            session.flush()
            print(f"创建了 {len(movies)} 部电影")

            # 创建电影-演员关联
            movie_actors = [
                MovieActor(movie_id=movies[0].id, actor_id=actors[1].id),  # 战狼2 - 吴京
                MovieActor(movie_id=movies[1].id, actor_id=actors[3].id),  # 李焕英 - 沈腾
                MovieActor(movie_id=movies[1].id, actor_id=actors[2].id),  # 李焕英 - 章子怡
                MovieActor(movie_id=movies[2].id, actor_id=actors[1].id),  # 流浪地球 - 吴京
                MovieActor(movie_id=movies[3].id, actor_id=actors[4].id),  # 少年的你 - 周冬雨
                MovieActor(movie_id=movies[4].id, actor_id=actors[1].id),  # 我和我的祖国 - 吴京
                MovieActor(movie_id=movies[4].id, actor_id=actors[5].id),  # 我和我的祖国 - 黄渤
            ]
            session.add_all(movie_actors)
            session.flush()
            print(f"创建了 {len(movie_actors)} 个电影-演员")
        except Exception as e:
            session.rollback()
            print(f"错误: {e}")

        session.commit()


def select_movieID_movie_category(movie_id: int):
    with Session() as session:
        stmt = select(Movie).where(Movie.id == movie_id)
        movie = session.scalar(stmt)
        print(movie)
        print(movie.category)
    pass


def select_movie_category():
    with Session() as session:
        stmt = select(Movie)
        movies = session.execute(stmt).scalars().all()
        for movie in movies:
            print(movie)
            print(movie.category)


def select_actorID_actor_profile(actor_id: int):
    with Session() as session:
        stmt = select(Actor).where(Actor.id == actor_id)
        actor = session.scalar(stmt)
        print(actor)
        print(actor.profile)
    pass


def select_movie_movieActor(movie_id: int):
    with Session() as session:
        stmt = select(Movie).where(Movie.id == movie_id)
        movie = session.scalar(stmt)
        print(movie)
        # print(movie.movieActors)
        for movieActor in movie.movieActors:
            print(movieActor.actor)
    pass


def select_actor_movieActor_movie(actor_id: int):
    with Session() as session:
        stmt = select(Actor).where(Actor.id == actor_id)
        actor = session.scalar(stmt)
        print(actor)
        for movieActor in actor.movieActors:
            print(movieActor.movie)


if __name__ == '__main__':
    # crete_table()
    # insert_test()
    # select_movieID_movie_category(1)
    # select_movie_category()
    # select_actorID_actor_profile(1)
    # select_movie_movieActor(2)
    # select_actor_movieActor_movie(2)
    pass

