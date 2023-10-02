from rest_framework import routers

from blog.views import PostViewSet, TipoViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'tipos_post', TipoViewSet)
