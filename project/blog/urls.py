from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('all_posts/',views.all_posts,name='all_posts'),
    path('post/<int:id>/',views.one_post,name='post'),
    path('create_post/',views.create_post,name='create_post'),
    path('<int:id>/edit/', views.edit_post, name='edit_post'),
]
