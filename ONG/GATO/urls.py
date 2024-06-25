from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('mascota/',views.mascota,name='mascota'),
    path('administracion/',views.admin,name='admin'),
    path('agregarMascota',views.agregarMascota,name='agregarMascota'),
    path('encontrarMascota/<str:pk>',views.encontrarMascota,name='encontrarMascota'),
    path('modificarMascota',views.modificarMascota,name='modificarMascota'),
    path('eliminarMascota/<str:pk>',views.eliminarMascota,name='eliminarMascota'),
    path('listadegatos',views.listadegatos, name='listadegatos'),
    path('listadeperros',views.listadeperros, name='listadeperros'),
]