from django.urls import path, include
from . import views
urlpatterns = [
    #仓库管理
    #跳转到仓库管理
    path('enter_wm/', views.enter_wmanagement),
    #添加仓库
    path('add_warehouse/', views.add_new_warehouse),
    #获得已添加的仓库信息
    path('get_warehouse_list/', views.get_warehouse_list)
]