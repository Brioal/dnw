from django.urls import path, include
from . import views
urlpatterns = [
    #跳转页面
    path('order/', views.testone),
    #获得表单信息的url
    path('getproduct/', views.get_product_json),
    #获得搜索提示的URL
    path('get_search_result/', views.search_auto_result)
]