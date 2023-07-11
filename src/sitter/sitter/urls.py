from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API Documentation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('seats.urls')),
    path('docs/', schema_view),
]
