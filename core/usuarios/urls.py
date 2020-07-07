from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views as v

urlpatterns = [
    path('', v.home),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', v.Login.as_view(), name='register'),
    path('accounts/', include('allauth.urls')), 
    # path('produtos/new/', v.cadastrar_produto, name='cadastro_produtos'),
    # path('produtos/', v.produtos, name='produtos'),
    # path('produtos/<int:pk>/', v.produtos_detalhe, name='produtos_detalhe'),
    # path('produtos/<int:pk>/compra/', v.compra_produto, name='compra_produto'),
    # path('produtos/finalizando/', v.finalizando_compra, name='finalizando_compra'),
    # path('produtos/excluir_item/<int:pk>/', v.exclui_item, name='exclui_item'),
    # path('produtos/add_carrinho/', v.add_carrinho),
    # path('produtos/excluir_produto/<int:pk>/', v.exclui_produto, name='exclui_produto'),
    # path('produtos/pagamento/', v.acesso_gateway, name="acesso_gateway"),
    # path('produtos/<int:pk>/edit/', v.produto_editar, name='produto_editar'),
]