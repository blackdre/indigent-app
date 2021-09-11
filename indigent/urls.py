from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(  # new
    openapi.Info(
        title="Indigent API",
        default_version="v1",
        description="An API for the Indigent data collection",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="sbu@sbutheitguy.co.za"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('community_data.urls')),
    path('auth/', include('djoser.urls')),
    path('', schema_view.with_ui(  # new
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
]
