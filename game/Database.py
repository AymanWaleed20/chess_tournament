from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DB:
    db_session = None

    def __new__(cls):
        if cls.db_session is None:
            engine = create_engine("mysql://root:Ayman1234@127.0.0.1/chess_game", echo=False, future=True)
            Session = sessionmaker(bind=engine)
            cls.db_session = Session()
        return cls.db_session

