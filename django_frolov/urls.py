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
from django.contrib import admin
from django.urls import path

from students import views as student_views
from group import views as group_views
from teachers import views as teacher_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', student_views.home),
    path('generate-student/', student_views.generate_student),
    path('generate-students/', student_views.generate_students),
    path('groups/', group_views.groups),
    path('teachers/', teacher_views.teachers),
]
