from django.urls import path
from crudapp import views



urlpatterns = [
    path('display', views.display, name="display"),
    path('create', views.create, name="create"),
    path('sample', views.sample, name="sample"),
    path('search', views.search, name="search"),
    path('home', views.home, name="home"),
    path('index', views.index, name="index"),
    path('', views.read, name="read"),
    path('update', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),

]