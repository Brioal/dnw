from django.urls import path, include
from . import views
urlpatterns = [
    #回访提示url
    path('backtips/', views.get_back),
    #回访列表URL
    path('backlist/', views.get_back_list),
    #跳转到回访列表
    path('go_backlist/', views.back_list),
    #确定回访后的接口
    path('determine_back/', views.set_back_state),


    #****添加回访计划**************************************************************
    #显示已添加的回访计划
    path('display_back_add/', views.get_add_back_list),
    path('search_display/', views.display_serach_back),
    path('add_back_plan/', views.save_back_plan),

    #历史回访记录里
    #展示所有历史回访记录
    path('display_history_record/', views.history_record),
    #日期及查询的URL
    path('history_search_record/', views.get_history_search_back)
]