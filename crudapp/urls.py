from django.urls import path
from crudapp import views



urlpatterns = [
   # path('display', views.display, name="display"),
    path('create', views.create, name="create"),
   # path('', views.home, name="home"),
    path('index', views.index, name="index"),
    path('read', views.read, name="read"),
    path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),

]