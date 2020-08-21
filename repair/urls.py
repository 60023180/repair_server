from django.urls import path, include
from rest_framework import routers
from repair import views

router = routers.DefaultRouter()
router.register('', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls))
]
