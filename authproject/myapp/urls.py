from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contacts/',views.contacts,name='contacts'),
    path('data_security/',views.data_security,name='data_security'),
    path('liscence_policy/',views.liscence_policy,name='liscence_policy'),
    path('user_aggrement/',views.user_aggrement,name='user_aggrement'),
    path('dashboard/',views.dashboard,name='dashboard'),
]
