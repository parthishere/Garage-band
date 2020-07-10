from rest_framework import routers
from .api import LinkraViewSet

router = routers.DefaultRouter()
router.register('api/Linkra',LinkraViewSet,'Linkra')

urlpatterns = router.urls
