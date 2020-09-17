from django.urls import path
from . import views
from . import api

app_name = 'job'
urlpatterns = [
    path('', views.job_lists, name='job_list'),
    path('add_job/', views.add_job, name='add_job'),
    path('user_favourites/',views.user_favourite,name='user_favourites'),
    path('<str:slug>/', views.job_details, name='job_detail'),
    path('<str:slug>/like_or_unlike/',views.like_or_unlike,name='like_or_unlike'),


    # Functional Based View
    path('api/list', api.job_list_api, name='job_list_api'),
    path('api/list/<int:id>/', api.job_detail_api, name='job_detail_api'),

    # Class Based View
    path('api/jobs/', api.Job_List_Api.as_view(), name='Job_List_Api'),
    path('api/jobs/Add/', api.Job_List_Api1.as_view(), name='Job_List_Api1'),
    path('api/jobs/<int:id>/', api.Job_Detail_Api.as_view(), name='Job_Detail_Api')
]
