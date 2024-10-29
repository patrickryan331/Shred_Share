from django.urls import path
from posts import views
from .views import CreatePostView, PostListView, create_comment, save_post_for_page, contact



urlpatterns = [
    path("details/<int:pk>/", views.PostDetailView.as_view(), name= 'details'),
    path("create/", CreatePostView.as_view(), name= "create_post"),
    path("posts/", PostListView.as_view(), name="posts"),
    path("create_comment", create_comment, name="create_comment"),
    path("save_comment", save_post_for_page, name="save_comment"),
    path("contact/", contact, name="contact"),
]