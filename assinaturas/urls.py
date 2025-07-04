from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_assinaturas, name='lista_assinaturas'),
    path('nova/', views.nova_assinatura, name='nova_assinatura'),
    path('<int:assinatura_id>/clientes/', views.assinatura_por_clientes, name='assinatura_por_clientes'),
]
