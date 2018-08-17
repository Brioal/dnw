from django.urls import path, include
from . import views
urlpatterns = [
    #跳转页面
    path('create/', views.testone),

    #项目创建
    path('api/create/', views.item_create),

]