from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from game.models import Tournament
import datetime
from .Database import DB


class UpcomingTournaments:

    @staticmethod
    def get_upcoming_tournaments():
        #engine = create_engine("mysql://root:Ayman1234@127.0.0.1/chess_game", echo=False, future=True)
        #Session = sessionmaker(bind=engine)
        db_session = DB()
        return db_session.query(Tournament).filter(Tournament.date > datetime.datetime.now()).all()

