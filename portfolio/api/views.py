from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, DestroyAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
# from rest_framework.filters import 
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from portfolio.models import UserProfileModel, User
from friendship.models import Follow, Block
from .serializers import ProfileRetrieveSerializer, ProfileCreateSerializer, FollowSerializer
from .permissions import IsOwnerOrReadOnly


class ProfileListAPIView(ListAPIView):
    queryset = UserProfileModel.objects.all()
    serializer_class = ProfileRetrieveSerializer
    permission_classes = []
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            obj_list = (
                Q(user__username__icontains=query) | Q(about__icontains=query) | Q(profession__icontains=query) | Q(softwear__icontains=query) | Q(awards__icontains=query)
            )
            queryset = UserProfileModel.objects.filter(obj_list).distinct()
            # context['query'] = query
            return queryset
        if query is None:
            return UserProfileModel.objects.all()

class ProfileRUDView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfileModel.objects.all()
    serializer_class = ProfileRetrieveSerializer
    permission_classes = [IsOwnerOrReadOnly,]

class ProfileCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]



@api_view(['POST', 'GET'])
def follow_create_api(request, pk):
    if request.method == 'GET':
        other_pk = request.data
        return Response({'data': other_pk})
    if request.method == 'POST':
        other_pk = request.data
        return Response({'data': other_pk})

# class FollowCreate(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         follow = Follow.objects.get(user=request.user)
#         serializer = SnippetSerializer(follow, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST



# class FollowerCreateAPI(CreateAPIView):
#     queryset = Follow.objects.all()
#     serializer_class = FollowSerializer
#     permission_class = [IsAuthenticatedOrReadOnly]

#     def get_queryset(self):
#         # queryset = 
#         return queryset


# class FollowerDestroyAPI(DestroyAPIView):
#     queryset = Follow.objects.all()
#     serializer_class = FollowSerializer
#     permission_class = [IsAuthenticatedOrReadOnly]

#     def get_queryset(self):
#         # queryset = 
#         return queryset

# class BlockCreateAPI(CreateAPIView):
#     queryset = Follow.objects.all()
#     serializer_class = FollowSerializer
#     permission_class = [IsAuthenticatedOrReadOnly]

#     def get_queryset(self):
#         # queryset = 
#         return queryset


# class BlockDestroyAPI(DestroyAPIView):
#     queryset = Follow.objects.all()
#     serializer_class = FollowSerializer
#     permission_class = [IsAuthenticatedOrReadOnly]

#     def get_queryset(self):
#         # queryset = 
#         return queryset

    