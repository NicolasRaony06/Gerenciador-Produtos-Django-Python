from django.urls import path
from . import views

urlpatterns = [
    path("cadastrar/", views.cadastrar),
    path("listar/", views.listar),
    path("deletar/<int:id>/", views.deletar)
]