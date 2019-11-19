from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('inna', views.inna, name='inna'),
    path('autorzy', views.autorzy, name='autorzy'),

]
