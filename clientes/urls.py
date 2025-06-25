from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('cadastrar/', views.cadastro_clientes, name='cadastro_clientes'),
    path('<int:cliente_id>/assinaturas/', views.cliente_assinaturas, name='cliente_assinaturas'),
]
