from sqlalchemy import create_engine, or_, and_, exists
from sqlalchemy.orm import sessionmaker, scoped_session
from game.models import *
import datetime
from .Database import DB


class TournamentsComponents:

    @staticmethod
    def get_upcoming_tournaments():
        # engine = create_engine("mysql://root:Ayman1234@127.0.0.1/chess_game", echo=False, future=True)
        # Session = sessionmaker(bind=engine)
        db_session = DB()
        return db_session.query(Tournament).filter(Tournament.date > datetime.datetime.now()).all()


class PlayerComponents:

    @staticmethod
    def my_matches(pk):
        db_session = DB()
        return db_session.query(Match).filter(or_(Match.player1_id == pk, Match.player2_id == pk)).all()

    @staticmethod
    def authenticate_player(data):
        db_session = DB()
        return bool(db_session.query(Player).filter(and_(Player.email == data['email'], Player.password == data['password'])).scalar())




