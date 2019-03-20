from django.shortcuts import render
from rest_framework import viewsets
from .models import ViewTeam
from .serializers import ViewTeamSerializer

class ViewTeamView(viewsets.ModelViewSet):
    queryset = ViewTeam.objects.all()
    serializer_class = ViewTeamSerializer