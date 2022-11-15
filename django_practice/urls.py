"""django_practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bboy.views import index, hello, form, BboyListAPIView, Bboy_data, \
    RegisterAPIView, LoginView, LogoutAPIView, BboyCreateAPIView, BboyUpdateAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index'),
    path('hello/', hello, name='hello'),
    path('form/', form, name='form'),
    path('api/', BboyListAPIView.as_view(), name='api'),
    path('funcapi/', Bboy_data, name='fucapi'),
    path('api/register/', RegisterAPIView.as_view(), name='Register API'),
    path('api/login/', LoginView.as_view(), name="Login API"),
    path('api/logout/', LogoutAPIView.as_view(), name='Logout API'),
    path('api/data/create', BboyCreateAPIView.as_view(), name='create API'),
    path('api/data/update/<int:pk>', BboyUpdateAPIView.as_view(), name='api update'),
]
