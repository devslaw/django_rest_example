# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'login/', views.Login.as_view(), name='login'),
    url(r'sign-up/', views.SignUpAPIView.as_view(), name='signup'),
    url(r'confirm-account/', views.ConfirmAccountAPIView.as_view(), name='confirm_account'),
    url(r'forgot-password/', views.ForgotPasswordAPIView.as_view(), name='forgot_password'),
    url(r'reset-password/(?P<reset_key>\w+)/$', views.ResetPasswordAPIView.as_view(), name='reset_password'),
]
