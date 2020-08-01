from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin

class ProfileListAPIView(ListAPIView):
    serializer_class = []
    