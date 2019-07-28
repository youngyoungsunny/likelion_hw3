from django.urls import path
from . import views

urlpatterns = [
    #path('new', views.new, name='new'),
    #path('create', views.create, name='create'),
    path('newblog/', views.blogpost, name='newblog'),
    path('<int:blog_id>', views.detail, name='detail'), #blog_id는 detail함수에 전달하는 인자 (detail에서 2번째 인자)
    path('<int:blog_id>/comment/new/', views.comment_new, name='comment_new'),
    path('<int:blog_id>/comment/<pk>/edit', views.comment_edit, name='comment_edit'),
    path('<int:blog_id>/comment/<pk>/delete/', views.comment_delete, name='comment_delete'),
]
