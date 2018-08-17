from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.carTypeView, name='index'),
    url(r'test', views.test, name='test')
]