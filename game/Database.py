from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DB:
    db_session = None

    def __init__(self):
        engine = create_engine("mysql://root:Ayman1234@127.0.0.1/chess_game", echo=False, future=True)
        Session = sessionmaker(bind=engine)
        db_session = Session()

    @staticmethod
    def getInstance():
        if DB.db_session is None:
            db_session = DB()

        return db_session
