from rest_framework import generics
from questions.models import Questions
from .serializers import (QuestionSerializer,QuestionCreateSerializer, QuestionListSerializer,UpvoteCreateSerializer,QuestionListDraftSerializer)
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from friendship.models import Follow
from portfolio.models import UserProfileModel
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

class QuestionDetailRudView(generics.RetrieveUpdateDestroyAPIView):
    authentication_clasees = (TokenAuthentication)
    lookup_field = 'pk'
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def get_queryset(self):
        return Questions.objects.all()

class QuestionCreateAPIView(generics.CreateAPIView):
    authentication_clasees = (TokenAuthentication)
    queryset = Questions.objects.all()
    serializer_class = QuestionCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class QuestionListAPIView(generics.ListAPIView):
    authentication_clasees = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PageNumberPagination
    serializer_class = QuestionListSerializer
    queryset = Questions.objects.all()
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('question','tags')

class QuestionDraftListAPIView(generics.ListAPIView):
    authentication_clasees = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PageNumberPagination
    serializer_class = QuestionListDraftSerializer
    queryset = Questions.objects.filter(draft=True)
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('question','tags')

class QuestionUovoteCreateView(generics.UpdateAPIView):
    authentication_clasees = (TokenAuthentication)
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def get_queryset(self):
        return Questions.objects.all()

# class QuestionSavedListAPIView(generics.ListAPIView):
#     authentication_clasees = (TokenAuthentication,)
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     pagination_class = PageNumberPagination
#     serializer_class = QuestionListSavedSerializer
#     queryset = SavedQuestion.objects.all()
#     filter_backends = (SearchFilter,OrderingFilter)
#     search_fields = ('question','tags')


    #
    # def get_context_data(self, **kwargs):
    #     request = self.request
    #     context = super(QuestionDraftListView, self).get_context_data(**kwargs)
    #     context["objects_list"] = Questions.objects.filter(user=request.user).filter(draft=True)
    #     return context
# from rest_framework.decorators import api_view
#
# @api_view()
# @permission_classes((permissions.AllowAny,))
# def upvote_create_api_view(self,request,*args,**kwargs):
#     pk = self.kwargs.get('pk')
#     request = request.user
#     serializer = UpvoteCreateSerializer
#     question_instance = Questions.objects.get(pk=pk)
#     if request.user in question_instance.like.all():
#         question_instance.like.remove(request)
#         if question_instance.like_count>=0:
#             question_instance.like_count -= 1
#         else:
#             question_instance.like_count = 0
#         question_instance.save()
#     else:
#         # u1 = UserProfileModel.objects.get(user=request.user)
#         question_instance.like.add(request.user)
#         if question_instance.like_count>=0:
#             question_instance.like_count += 1
#         else:
#             question_instance.like_count = 0
#         question_instance.save()
#     return Response(serializer.data)