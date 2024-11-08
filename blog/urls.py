from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.blog_list, name='blog-list'),
    path('detail/<int:post_id>/', views.blog_detail, name='blog-detail'),
]