"""
URL configuration for typeidea project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,re_path

from blog.views import post_list,post_detail
from config.views import links
from .custom_site import custom_site


urlpatterns = [
    re_path(r'^$',post_list),
    re_path(r'^category/(?P<category_id>\d+)/$',post_list),
    re_path(r'^tags/(?P<tag_id>\d+)/$',post_list),
    path('post/<int:post_id>.html',post_detail),
    re_path(r'^links/$',links),
    re_path(r'^super_admin/',admin.site.urls),
    re_path(r'^admin/', custom_site.urls)
]
