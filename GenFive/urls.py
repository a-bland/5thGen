from django.contrib import admin
from django.urls import path, include

from CharacterCreator import views
#from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'characters', views.CharacterViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('creation', views.creation),
    path('battle', views.battle),
]

#urlpatterns += router.urls
