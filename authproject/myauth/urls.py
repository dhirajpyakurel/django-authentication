from django.urls import path
from . import views
from django.urls import path
from .views import password_reset_request, password_reset_confirm

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('password-reset/', password_reset_request, name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
]


