from django.urls import path
from first_up import views

urlpatterns = [
    path ('', views.index, name='index'),
    
]