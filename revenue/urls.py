from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()

router.register('', views.RevenueStatisticViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "revenue"


