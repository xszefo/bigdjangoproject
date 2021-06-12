"""bigdjangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'devices'
urlpatterns = [
    path('', views.ListDevices.as_view(), name='list_devices'),
    path('create/', views.CreateDevice.as_view(), name='create_device'),
    path('ip-pools/', views.ListIpAddressPool.as_view(), name='ip_pools-list'),
    path('ip-pools/create', views.CreateIpAddressPool.as_view(), name='ip_pools-create'),
    path('ip-pools/delete/<int:pk>', views.DeleteIpAddressPool.as_view(), name='ip_pools-delete'),
    path('ip-pools/update/<int:pk>', views.UpdateIpAddressPool.as_view(), name='ip_pools-update'),
    path('update/<str:slug>/', views.UpdateDevice.as_view(), name='update_device'),
    path('delete/<str:slug>/', views.DeleteDevice.as_view(), name='delete_device'),
]
