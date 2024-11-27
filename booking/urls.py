from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('reservation/', views.reservation, name='reservation'),  
    path('reservation/confirm/<str:reservation_number>/', views.confirm_reservation, name='confirm_reservation'),  
]
