from rest_framework.generics import ListAPIView

from GenFive.serializers import CharacterSerializer
from CharacterCreator.models import Character

class ProductList(ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer