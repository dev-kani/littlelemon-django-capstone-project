from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/restaurant/', include('restaurant.urls')),
    path('admin/', admin.site.urls),
    # Generate a Token
    # path('api-token-auth/', obtain_auth_token)
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]
