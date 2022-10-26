from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name = 'Home'),
    path('Mars', views.Mars, name= 'Mars'),
    path('Earth', views.Earth, name = 'Earth')
]
