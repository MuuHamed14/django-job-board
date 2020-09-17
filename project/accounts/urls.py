from django.urls import path
from . import views
from .import api

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),

    # Functional Based View
    path('api/profile/',api.profiles,name='api_profile'),
    path('api/profile/<int:id>/',api.profiles_id,name='api_profile_id'),

    # Class Based View
    path('api/profiles/', api.Profile_Api.as_view(), name='Profile_Api'),
    path('api/profiles/Add/', api.Profile_Api1.as_view(), name='Profile_Api1'),
    path('api/profiles/<int:id>/', api.Profile_Api2.as_view(), name='Profile_Api2')
]
