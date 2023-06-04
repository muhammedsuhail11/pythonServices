from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet,ModelViewSet,GenericViewSet
from api.serializers import UserSerializer
from rest_framework.mixins import CreateModelMixin
from rest_framework import authentication,permissions
from rest_framework import serializers

# Create your views here.
class UsersView(GenericViewSet,CreateModelMixin):
    serializer_class=UserSerializer
    queryset=User.objects.all()
