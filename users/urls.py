from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register', views.signup_view, name='signup_page'),
    path('logout', views.logout_view, name="logout_page"),
    re_path('^login/$', auth_views.LoginView.as_view(template_name='users/login.html'), name="login_page"),
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(template_name='users/change_password.html', success_url="/"),
        name="change_password_page"
    )
]
