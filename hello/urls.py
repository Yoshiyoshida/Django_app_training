#hello-app独自にurlを管理したい

from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('next', views.next, name='next'),
]
