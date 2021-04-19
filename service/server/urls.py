from django.conf.urls import url, include
from server.views import PersonViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PersonViewSet, base_name="person")

urlpatterns = [
    url('', include(router.urls))
]

