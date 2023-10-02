from rest_framework import routers

from classificados import views

router = routers.DefaultRouter()
router.register(r'empresas', views.EmpresaViewSet)
router.register(r'prospectos', views.ProspectoViewSet)
router.register(r'categorias', views.CategoriaViewSet)
