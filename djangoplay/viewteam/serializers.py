from rest_framework import serializers
from .models import ViewTeam

class ViewTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewTeam
        fields = ('id', 'name', 'github', 'funfact')