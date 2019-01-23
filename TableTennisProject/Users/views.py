from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Player, Group
from .serializers import PlayerSerializer, GroupSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class LoginViewSet(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        token = Token.objects.get(user=request.user)
        print(token.id)
        return True


class TokenAdminView(APIView):

    def get(self, request):
        for user in User.objects.all():
            Token.objects.get_or_create(user=user)

        return Response(data="Successfull", status=status.HTTP_200_OK)
