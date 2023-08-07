from django.urls import path
from .views import UserListCreateView, SeatListCreateView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('seats/', SeatListCreateView.as_view(), name='seat-list'),
]
