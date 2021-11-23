from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views
from django.conf.urls import url

router = SimpleRouter()

urlpatterns = [
    path('', views.hello, name='hello'),
    path('menu/post_list', views.post_list, name='post_list'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    path('blog/menu/', views.main_menu, name='main_menu'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    #path('post/best/<int:pk>/', views.best_post, name='best_post'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('register/', views.register, name='register'),
    path('post/<int:pk>/leave_comment/', views.post_detail, name='leave_comment'),
    path('like/<int:pk>/', views.LikeView, name='like_post'),
    path('login/', views.login_user, name='login'),
    path('category/<str:cats>/', views.category_view, name='category')
]