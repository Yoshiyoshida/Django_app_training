#hello-app独自にurlを管理したい

from django.urls import path
from . import views

urlpatterns = [
    
    path('<int:id>/<nickname>/', views.index, name='index'),
    path('test', views.test, name='test'),
]
