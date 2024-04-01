from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import NoteSerializer
from .models import Note


@api_view(['GET'])
def NoteApis(request):
    url_partten = {
        'NoteList': '/note-list/',
        'NoteDetail': '/note-detail/<str:pk>/',
        'CreateNote': '/createnote/',
        'UpdateNote': '/updatenote/<str:pk>/',
        'DeleteNote': '/deletenote/<str:pk>/',
    }
    return Response(url_partten)


@api_view(['GET'])
def NoteList(request):
    note = Note.objects.all()
    seriaizer = NoteSerializer(note, many= True)
    return Response(seriaizer.data)


@api_view(['GET'])
def NoteDetail(request, pk):
    note = Note.objects.get(id = pk)
    serializer = NoteSerializer(note, many= False)
    return Response(serializer.data)



@api_view(['POST'])
def CreateNote(request):
    serializer = NoteSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def UpdateNote(request, pk):
    note = Note.objects.get(id= pk)
    serializer = NoteSerializer(instance= note, data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


def DeleteNote(request, pk):
    note = Note.objects.get(id= pk)
    note.delete()
    return Response('Item Deleted Successfully')




