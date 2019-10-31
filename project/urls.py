from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView

API_TITLE = 'REST API Documentation.'
API_DESCRIPTION = 'Documentation for REST API.'

schema_view = get_schema_view(
    openapi.Info(
         title=API_TITLE,
         default_version='v1',
         description=API_DESCRIPTION,
         contact=openapi.Contact(email="admin@admin.ru"),
    ),
    public=False,
    permission_classes=(permissions.IsAdminUser,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/', include('core.urls')),

    path(
        'swagger-docs/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
]
