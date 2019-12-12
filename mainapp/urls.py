
from django.contrib import admin
from django.urls import path, include
from mainapp.views import *

urlpatterns = [
    path('', index,name='index'),
    path('contestant', contestant, name='contestant'),
    path('schedule', schedule, name='schedule'),
    path('partners', partners, name='partners'),
    path('crew', crew, name='crew'),
    path('reg_form', reg_form, name= 'reg_form'),
    path('dashboard', dashboard, name='dashboard'),
    path('success', success, name='success')
]
