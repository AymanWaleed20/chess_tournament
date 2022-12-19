
from game.models import Tournament
import datetime
from .Database import DB


class UpcomingTournaments:

    @staticmethod
    def get_upcoming_tournaments():
        database_connection = DB.getInstance()
        return database_connection.query(Tournament).filter(Tournament.date > datetime.datetime.now()).all()

