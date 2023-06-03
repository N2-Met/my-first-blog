from django.urls import path
from . import views


# post_list という名前の ビュー をルートURLに割り当てる
urlpatterns = [
    path('', views.post_list, name='post_list'),
    # もし post/何かしらの数字/ の形のURLがリクエストされたら、post_detail ビューを呼び出し、
    # そのビューにパラメータとして pk を渡す" というルールを Django に教えています。そして、このルールの名前は post_detail です。
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
