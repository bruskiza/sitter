from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import User, Seat
from .serializers import UserSerializer, SeatSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SeatListCreateView(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
