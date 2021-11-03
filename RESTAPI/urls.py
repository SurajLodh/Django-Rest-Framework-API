from RESTAPI.models import Student
from django.contrib import admin
from django.db import router
from django.urls import path
from django.urls.conf import include

#custom need Import 
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

#Default Router
router = DefaultRouter()

#using Deafult_Router We route aur view Class 
router.register('student', views.StudentViewSet, basename="student")

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path('auth/', include('rest_framework.urls', namespace="Authentication")),
    path('gettoken/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('refreshtoken/', TokenRefreshView.as_view(), name="token_refresh"),
    path('verifytoken/', TokenObtainPairView.as_view(), name="token_verify"),
    path('', include(router.urls)),


]