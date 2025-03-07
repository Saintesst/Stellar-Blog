from django.urls import path
from .views import register,profile, edit_profile, user_logout, user_search, profile_view, CustomLoginView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('user_search/', user_search, name='user_search'),
    path("profile/<str:username>/", profile_view, name="profile"),
]
