 
from django.urls import path
from .views import *

urlpatterns = [
path('stulist/', Stulist.as_view()),
path('studetail/<int:pk>/',Studetail.as_view())
]