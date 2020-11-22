"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from addressApp.api.viewsets import AddressViewSet
from clientsApp.api.viewsets import ClientViewSet
from flavorsApp.api.viewsets import FlavorViewSet
from ordersApp.api.viewsets import OrderViewSet
from pizzasApp.api.viewsets import PizzaViewSet
from sizesApp.api.viewsets import SizeViewSet
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'address', AddressViewSet)
router.register(r'client', ClientViewSet)
router.register(r'flavor', FlavorViewSet)
router.register(r'order', OrderViewSet)
router.register(r'pizza', PizzaViewSet)
router.register(r'size', SizeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
