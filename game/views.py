from django.http import HttpResponse
from rest_framework.decorators import action
from game.serializers import TournamentSchema
from rest_framework import viewsets
from game.components import UpcomingTournaments


class TournamentViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['GET'], url_path="")
    def upcoming_tournaments(self, request):
        tournaments = UpcomingTournaments.get_upcoming_tournaments()
        schema = TournamentSchema(many=True)
        result = schema.dumps(tournaments)
        return HttpResponse(result)

