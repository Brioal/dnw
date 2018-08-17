"""vin码查询 URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from indexpage.views import index_page


urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^$', index_page),
    url(r'^vin_search/', include('vin_search.urls')),
    # url(r'^admin/users/myuser/add/', include('users.urls')),
    url(r'^admin/', admin.site.urls),
    #开产品和项目
    path('product/', include('product.urls')),
    #项目录入
    path('items/', include('items.urls')),
    #回访计划
    path('back_plan/', include('returnvisit.urls'))

]
