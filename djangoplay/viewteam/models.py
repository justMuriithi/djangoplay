from django.db import models


class ViewTeam(models.Model):
    name = models.CharField(max_length=50)
    github = models.CharField(max_length=50)
    funfact = models.CharField(max_length=50)
