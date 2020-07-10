from Linkra.models import Linkra
from rest_framework import viewsets , permissions
from .serializers import LinkraSerializer

class LinkraViewSet(viewsets.ModelViewSet):
    queryset = Linkra.objects.all()
    permission_classes = [
     permissions.AllowAny
    ]
    serializer_class = LinkraSerializer
