from rest_framework import viewsets
from GenFive.serializers import UserSerializer, GroupSerializer, CharacterSerializer
from rest_framework import permissions
from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User, Group
from CharacterCreator.models import Character, User
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'home.html')


def creation(request):
    return render(request, 'creation.html')


def battle(request):
    return render(request, 'battle.html')


# from django.contrib.auth.models import User, Group

class UserViewSet(viewsets.ModelViewSet):
    # API endpoint that allows users to be viewed or edited.
    # queryset = User.objects.all().order_by('-date_joined')
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    # API endpoint that allows groups to be viewed or edited.
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticated]
