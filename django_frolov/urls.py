"""django_frolov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import debug_toolbar

from django.contrib import admin
from django.urls import include, path

from .views import error_404, error_500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('accounts.urls')),
    path('', include('general.urls')),
    path('', include('students.urls')),
    path('', include('groups.urls')),
    path('', include('teachers.urls')),
    path('', include('contact_us.urls')),
    path('', include('currency.urls')),
    path('__debug__/', include(debug_toolbar.urls))
]

handler404 = error_404
handler500 = error_500
