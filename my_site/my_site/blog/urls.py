from django.urls import path
from . import views

urlpatterns = [
    path("", view.starting_page, name="starting_page"),
    path("posts/", views.posts, name="posts-page"),
    path("posts/<slug>", views.post_detail, name="post-detail-page")
]
