"""page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from wedpage import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    url(r'^home',views.home,name='home'),
    url(r'^benefits',views.benefits, name='benefits'),
    url(r'^card',views.card ,name='card'),
    url(r'^customer-management',views.CustomerManagement ,name='customer-management'),
    url(r'^featurepage',views.featurepage,name='featurepage'),
    url(r'^login',views.login,name='login'),
    url(r'^vlog',views.vlog ,name='vlog'),
    url(r'^contactus',views.contactus,name='contactus'),
    url(r'^ecommerce',views.ecommerce,name='ecommerce'),
    url(r'^stored-value-cards',views.StoredValueCards,name='stored-value-cards'),
    url(r'^POS3',views.POS3,name='POS3'),
    url(r'^inventory',views.inventory,name='inventory'),
    url(r'^staff-management',views.StaffManagement ,name='staff-management'),
    url(r'^shipping',views.shipping ,name='shipping'),
]
