from django.urls import path, include
from . import views
urlpatterns = [
    #回访提示url
    path('backtips/', views.get_back),
    #回访列表URL
    path('backlist/', views.get_back_list),
    #跳转到回访列表
    path('go_backlist/', views.back_list)
]