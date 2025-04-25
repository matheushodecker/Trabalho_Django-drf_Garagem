from rest_framework.viewsets import ModelViewSet

from core.models import Modelo

class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = Modelo