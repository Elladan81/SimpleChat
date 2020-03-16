from django.urls import path

from . import views

urlpatterns = [
    path('/join_room/', views.join_room, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]
