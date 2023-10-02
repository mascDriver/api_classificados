from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticated

from .models import Post, Tipo
from .serializers import PostSerializer, TipoSerializer


class PostViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['tipo']
    search_fields = ['titulo', 'tipo__slug']
    ordering_fields = ['titulo', 'tipo']
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get(slug=self.kwargs['pk'])
        return obj


class TipoViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['nome', 'slug']
    search_fields = ['slug']
    ordering_fields = ['nome', 'slug']
    permission_classes = [IsAuthenticated]
