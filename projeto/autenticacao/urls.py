from django.urls import path  
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path("login/", fazer_login, name='fazer_login'),
    path("logout/", fazer_logout, name='fazer_logout'),
    path("criarconta/", criar_conta, name='criar_conta'),
    path("passwordchange/", views.PasswordChangeView.as_view(), name="password_change"),
    path("passwordchange/done/", views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("passwordreset/", views.PasswordResetView.as_view(), name="password_reset"),
    path("passwordreset/done/", views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]