from rest_framework import generics
from answers.models import Answers
from .serializers import AnswerSerializer,AnswerCreateSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from friendship.models import Follow
from portfolio.models import UserProfileModel
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

class AnswerDetailRudView(generics.RetrieveUpdateDestroyAPIView):
    authentication_clasees = (TokenAuthentication)
    lookup_field = 'pk'
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def get_queryset(self):
        return Answers.objects.all()

class AnswerCreateAPIView(generics.CreateAPIView):
    authentication_clasees = (TokenAuthentication)
    queryset = Answers.objects.all()
    serializer_class = AnswerCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)