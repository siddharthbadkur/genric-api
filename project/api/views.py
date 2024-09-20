from django.shortcuts import render 
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics



class Stulist(generics.ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer


class Studetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

