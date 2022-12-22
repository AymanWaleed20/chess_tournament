from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import action
from game.serializers import TournamentSchema, MatchSchema, PlayerSchema
from rest_framework import viewsets
from game.components import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class TournamentViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['GET'], url_path="")
    def upcoming_tournaments(self, request):
        tournaments = TournamentsComponents.get_upcoming_tournaments()
        schema = TournamentSchema(many=True)
        result = schema.dump(tournaments)
        return JsonResponse({"data": result})


class PlayerViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['GET'], url_path="")
    def my_matches(self, request, pk=None):
        matches = PlayerComponents.my_matches(pk)
        schema = MatchSchema(many=True)
        result = schema.dump(matches)
        return JsonResponse({"data": result})


class LoginView(APIView):

    def post(self, request):
        flag = PlayerComponents.authenticate_player(request.data)
        if flag:
            authenticate()
            contex = {
                'response': "authenticated"
            }
            return JsonResponse(contex)
        else:
            contex = {
                'response': "email or password is not correct"
            }
        return JsonResponse(contex)
