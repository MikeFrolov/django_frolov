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

from group import views as groups_views

from students import views as students_views

from teachers import views as teachers_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', students_views.home),
    path('generate-student/', students_views.generate_student),
    path('generate-students/', students_views.generate_students),
    path('create_student_form/', students_views.create_student_form),
    path('create_group_form/', groups_views.create_group_form),
    path('create_teacher_form/', teachers_views.create_teacher_form),
    path('list_students/', students_views.list_filtered_students),
    path('list_groups/', groups_views.list_groups),
    path('list_teachers/', teachers_views.list_filtered_teachers),
]
