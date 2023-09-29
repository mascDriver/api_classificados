from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticated

from .models import Empresa, Prospecto, Categoria
from .serializers import EmpresaSerializer, ProspectoSerializer, CategoriaSerializer


class EmpresaViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['categoria']
    search_fields = ['categoria__slug']
    ordering_fields = ['nome', 'email']
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get(slug=self.kwargs['pk'])
        return obj


class ProspectoViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Prospecto.objects.all()
    serializer_class = ProspectoSerializer
    permission_classes = [IsAuthenticated]


class CategoriaViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['nome', 'slug']
    search_fields = ['slug']
    permission_classes = [IsAuthenticated]

