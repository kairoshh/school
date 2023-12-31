
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mainapp.urls')),
]
