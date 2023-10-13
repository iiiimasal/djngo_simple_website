from django.urls import path
from . import views

urlpatterns=[
    path('projects/',views.projects,name="projects"), 
    path('project/<str:pk>',views.project,name="project"),
    path('',views.home,name="room"),
    path('room/<str:pk>',views.room,name='rooms'),
    path('create-room/',views.createRoom,name='create-room'),
    path('update-room/<str:pk>/',views.updateRoom,name='update-room'),
    path('delete-room/<str:pk>/',views.deleteRoom,name='delete-room')
]