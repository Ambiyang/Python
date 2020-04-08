'''
store应用urls文件
'''

from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path('^$|^login/$', views.login, name='login_view'),
    path('logout/', views.logout, name='logout_view'),
    path('register/', views.register, name='register_view'),
    path('main/', views.main, name='main_view'),
    path('list/', views.GoodsListView.as_view(), name='list_view'),
    path('detail/', views.show_goods_detail, name='detail_view'),
    path('add/', views.add_cart),
    path('show_cart/', views.show_cart, name='cart_view'),
    path('submit_orders/', views.submit_orders),
]
