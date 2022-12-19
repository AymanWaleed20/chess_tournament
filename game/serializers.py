from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from game.models import *


class ClubSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Club
        include_relationships = True
        load_instance = True


class PlayerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Player
        include_relationships = True
        include_fk = True
        load_instance = True


class TournamentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Tournament
        include_relationships = True
        include_fk = True
        load_instance = True


class MatchSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Match
        include_fk = True
        load_instance = True


class PlayerTournamentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PlayerTournament
        include_fk = True
        load_instance = True


