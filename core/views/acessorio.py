from core.serializers.acessorio import AcessorioSerializer
from rest_framework.viewsets import ModelViewSet

from core.models import Acessorio


class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer