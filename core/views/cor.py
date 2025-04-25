from rest_framework.viewsets import ModelViewSet

from core.models import Cor


class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = Cor