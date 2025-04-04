from django.contrib import admin
from django.urls import path
from main.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Omborxona API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

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

    path('swagger_format/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
