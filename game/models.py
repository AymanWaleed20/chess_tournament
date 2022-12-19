from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Club(Base):
    __tablename__ = "club"

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    address = Column(String(20))
    tel_number = Column(Integer)
    # hosted_matches = Column(Integer)
    # players = relationship("Player", back_populates="club")   , cascade="all, delete-orphan
    players = relationship("Player", backref="club")
    tournaments = relationship("Tournament", backref="club")

    def __repr__(self):
        return f"Club(id={self.id!r}, name={self.name!r}, address={self.address!r}," \
               f" tel_num={self.tel_num!r})"


class Player(Base):
    __tablename__ = "player"

    id = Column(Integer, primary_key=True)
    club_id = Column(Integer, ForeignKey("club.id"), nullable=False)
    name = Column(String(20))
    email = Column(String(20))
    phone_number = Column(Integer)
    # played_matches = Column(Integer)
    # club = relationship("Club", back_populates="players")
    #matches = relationship("Match", backref="player")
    players_tournaments = relationship("PlayerTournament", backref="player")

    def __repr__(self):
        return f"Club(id={self.id!r}, name={self.name!r}, email={self.email!r}," \
               f" phone_number={self.phone_number!r})"


class Tournament(Base):
    __tablename__ = "tournament"

    id = Column(Integer, primary_key=True)
    club_id = Column(Integer, ForeignKey("club.id"), nullable=False)
    name = Column(String(20))
    date = Column(DateTime)
    matches = relationship("Match", backref="tournament")
    players_tournaments = relationship("PlayerTournament", backref="tournament")

    def __repr__(self):
        return f"Club(id={self.id!r}, name={self.name!r},)" \



class PlayerTournament(Base):
    __tablename__ = "player_tournament"

    player_id = Column(Integer, ForeignKey("player.id"), primary_key=True)
    tournament_id = Column(Integer, ForeignKey("tournament.id"), primary_key=True)
    date_of_join = Column(DateTime)


class Match(Base):
    __tablename__ = "match"

    id = Column(Integer, primary_key=True)
    player1_id = Column(Integer, ForeignKey("player.id"), nullable=False)
    player2_id = Column(Integer, ForeignKey("player.id"), nullable=False)
    tournament_id = Column(Integer, ForeignKey("tournament.id"), nullable=False)
    date_of_match = Column(DateTime)

    player1_ = relationship("Player", foreign_keys=[player1_id])
    player2_ = relationship("Player", foreign_keys=[player2_id])


#engine = create_engine("mysql://root:Ayman1234@127.0.0.1/chess_game", echo=True, future=True)
#Base.metadata.create_all(engine)
