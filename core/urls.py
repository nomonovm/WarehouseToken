from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sotuvchi/', SotuvchiListCreateView.as_view()),
    path('sotuvchi/<int:pk>/', SotuvchiRetrieveUpdateDestroyView.as_view()),
    path('mahsulotlar/', MahsulotListCreateView.as_view()),
    path('mahsulotlar/<int:pk>/', MahsulotRetrieveUpdateDestroyView.as_view()),
    path('mijozlar/', MijozListCreateView.as_view()),
    path('mijozlar/<int:pk>/', MijozRetrieveUpdateDestroyView.as_view()),
    path('sotuv/', SotuvListCreateView.as_view()),
    path('sotuv/<int:pk>/', SotuvRetrieveUpdateDestroyView.as_view()),
    path('bolimlar/', BolimListCreateView.as_view()),
]
