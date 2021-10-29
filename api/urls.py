from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'labels', LabelViewSet)
router.register(r'pains', PainViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('/api-auth/', include('rest_framework.urls')),
    path('search/', include('haystack.urls'))
]
