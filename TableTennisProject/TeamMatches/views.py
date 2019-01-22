import json

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Team, Match, Set, SET_CHOICE
from .serializers import TeamSerializer, MatchSerializer, SetSerializer

from utils.mixins import error_msg_string


# Create your views here.


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class SetViewSet(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer

    def list(self, request, *args, **kwargs):

        if 'match' in request.query_params or 'set_name' in request.query_params:
            if 'match' in request.query_params and 'set_name' in request.query_params:
                obj, created = Set.objects.get_or_create(
                    match_id=request.query_params['match'],
                    set_name=request.query_params['set_name'],
                    defaults={'match_id': request.query_params['match'],
                              'set_name': request.query_params['set_name']},
                )
                new_serializer_data = SetSerializer(obj).data
            elif 'match' in request.query_params:
                queryset = Set.objects.filter(match_id=request.query_params['match'])

                serializer_data = SetSerializer(queryset, many=True).data
                set_details = list(serializer_data)
                match_data = Match.objects.get(id=int(request.query_params['match'])).match_status

                new_serializer_data = dict()
                new_serializer_data['set_details'] = set_details
                new_serializer_data['match_status'] = match_data

        else:
            queryset = self.queryset
            new_serializer_data = SetSerializer(queryset, many=True).data

        return Response(data=new_serializer_data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = SetSerializer(data=request.data)
        if serializer.is_valid():
            obj, created = Set.objects.update_or_create(
                match_id=request.data['match'], set_name=request.data['set_name'],
                defaults={'match_id': request.data['match'],
                          'set_name': request.data['set_name']})

            obj.team1_score = request.data['team1_score']
            obj.team2_score = request.data['team2_score']
            obj.save()

            set_serializer = SetSerializer(obj).data
            return Response(data=set_serializer, status=status.HTTP_200_OK)
        else:
            return Response('HTTP_400_BAD_REQUEST', 'INVALID_CREATE',
                            serializer.errors)


class SetNameViewSet(APIView):

    def get(self, request):
        setname_list = []
        setname_dict = {}

        for key in SET_CHOICE:
            setname_dict['set_name'] = key[1]
            setname_dict['set_value'] = key[0]
            setname_list.append(setname_dict)
            setname_dict = {}

        return Response(data=setname_list, status=status.HTTP_200_OK)
