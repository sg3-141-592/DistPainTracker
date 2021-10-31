from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

router = routers.DefaultRouter()

router.register(r'labels', LabelViewSet)
router.register(r'pains', PainViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('search/', include('haystack.urls'))
]
