"""TableTennisProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.authtoken import views

from TeamMatches.views import SetNameViewSet
from Users.views import TokenAdminView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('userdetails/', include('Users.urls')),
    path('matchdetails/', include('TeamMatches.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('set_name_list/', SetNameViewSet.as_view()),
    path('generate_token/', TokenAdminView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
