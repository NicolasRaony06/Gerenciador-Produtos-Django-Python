from django.urls import path
from . import views

urlpatterns = [
    path("cadastrar/", views.cadastrar),
    path("listar/", views.listar, name='listar'),
    path("deletar/<int:id>/", views.deletar),
    path("alterar/<int:id>/", views.alterar, name='alterar')
]