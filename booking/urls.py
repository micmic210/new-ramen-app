from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('philosophy/', views.philosophy, name='philosophy'),
    path('reservation/confirm/<str:reservation_number>/', views.confirm_reservation, name='confirm_reservation'),  
    path('reservation/', views.reservation, name='reservation'),  
    path('contact/', views.contact, name='contact'),
]
