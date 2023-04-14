
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from home.Mobviewset import MobViewSet
router = routers.DefaultRouter()
router.register(r'Mobproduct',MobViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(router.urls))
]