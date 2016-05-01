"""kidgames URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^k5/', include('k5.urls')),
	url(r'^k6/', include('k6.urls')),
	url(r'^k7/', include('k7.urls')),
	url(r'^k8/', include('k8.urls')),
	url(r'^l1/', include('l1.urls')),
	url(r'^l2/', include('l2.urls')),
    url(r'^admin/', admin.site.urls),
]
