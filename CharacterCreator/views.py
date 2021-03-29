from rest_framework import viewsets
from GenFive.serializers import UserSerializer, PartiesSerializer, CharacterSerializer
from rest_framework import permissions
from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User, Group
from CharacterCreator.models import Character, User, Parties
from django.views.decorators.csrf import csrf_exempt


def home(request):
    parties = Parties.objects
    characters = Character.objects
    return render(request, 'home.html', {'parties': parties, 'characters': characters})


def login(request):
    allUsers = User.objects
    return render(request, 'login.html', {'allUsers': allUsers})


def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')


def creation(request):
    return render(request, 'creation.html')


def battle(request):
    party = Parties.objects.get(pk=1)
    character = Character.objects.get(pk=18)
    return render(request, 'battle.html', {'party': party, 'character': character})


class UserViewSet(viewsets.ModelViewSet):
    # API endpoint that allows users to be viewed or edited.
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PartiesViewSet(viewsets.ModelViewSet):
    # API endpoint that allows Parties to be viewed or edited.
    queryset = Parties.objects.all()
    serializer_class = PartiesSerializer
    permission_classes = [permissions.IsAuthenticated]


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticated]
