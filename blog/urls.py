from django.urls import path
from . import views

urlpatterns = [
    path("post/new/", views.create_post, name="create_post"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("post/<int:post_id>/publish/", views.publish_post, name="publish_post"),
    path("", views.post_list, name="post_list"),
]