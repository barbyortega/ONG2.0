from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('listadegatos',views.listadegatos, name='listadegatos'),
    path('listadeperros',views.listadeperros, name='listadegatos'),
    path('lara',views.lara, name='lara'),
    path('marcos',views.marcos, name='marcos'),
    path('mia',views.mia, name='mia'),
    path('fido',views.fido, name='fido'),
    path('Max',views.Max, name='Max'),
    path('Tobi',views.Tobi, name='Tobi'),
]