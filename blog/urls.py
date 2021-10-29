from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('register/', views.register, name='register'),
    path('post/<int:pk>/leave_comment/', views.post_detail, name='leave_comment'),
    url(r'^(?P<slug>S+)/addlike/$', views.add_like, name='add_like'),
    url(r'^(?P<slug>S+)/adddislike/$', views.add_dislike, name='add_dislike'),
]
