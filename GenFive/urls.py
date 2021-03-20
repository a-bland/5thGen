from django.contrib import admin
from django.urls import path

from CharacterCreator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('creation', views.creation),
    path('battle', views.battle),
    path('my-ajax-test/', views.testcall),
]