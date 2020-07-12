from rest_framework import routers
from .api import LinkraViewSet
from .views import QuestionCreate

app_name='questions'

router = routers.DefaultRouter()
router.register('api/Linkra',LinkraViewSet,'Linkra')


urlpatterns = [
	path('', QuestionCreate.as_view(), name='ask-question')
]

urlpatterns += router.urls

