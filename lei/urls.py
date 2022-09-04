from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('news-list/', views.newsList, name='news-list'),
    path('recursos-list/', views.recursoList, name='recursos-list'),
    path('notas-list/', views.notaList, name='notas-list'),

    path('recursos-detail/<str:pk>/', views.recursoDetail, name='recurso-detail'),

    path('calendario-list/', views.calendarioList, name='calendario-list'),
]
