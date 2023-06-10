from django.urls import path
from accounts import views


app_name = 'accounts'

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("request-reset-password-form/", views.requestResetPassword, name='request-reset-password-form'),
    path("password_reset_confirm/<uidb64>/<token>", views.password_reset_confirm, name="password_reset_confirm"),
    path("activate/<uidb64>/<token>",  views.ActivateAccountView.as_view(), name='activate'),
]