from django.urls import path
from .views import register, user_login, profile, edit_profile, user_logout, user_search

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('user_search/', user_search, name='user_search'),
]
