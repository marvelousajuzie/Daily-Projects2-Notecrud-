from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoteApis, name= 'NoteApis'),
    path('NoteList/', views.NoteList, name= 'NoteList'),
    path('NoteDetail/<str:pk>/', views.NoteDetail, name= 'NoteDetail'),
    path('CreateNote/', views.CreateNote, name= 'CreateNote'),
    path('UpdateNote/<str:pk>/', views.UpdateNote, name= 'UpdateNote'),
    path('DeleteNote/<str:pk>/', views.DeleteNote, name= 'DeleteNote'),
]
