from django.contrib.auth import views as auth_views
from django.urls import path

from .views import password_reset_view
from .views import sign_up_view, login_view, logout_view, change_password


urlpatterns = [
    path('signup/', sign_up_view, name='signup'),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('change_password/', change_password, name='change_password'),
    path('password_reset/', password_reset_view, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
