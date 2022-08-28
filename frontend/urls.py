from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('lei/', views.lei, name="lei"),
    path('news/', views.news, name="news"),
    path('recursos/', views.recursos, name="recursos"),
    path('calendario/', views.calendario, name="calendario"),
    path('notas/', views.notas, name="notas"),


]