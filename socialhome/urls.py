"""URLs file for the app SocialHome"""

from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name = "homepage"),
    path("add_post/", PostCreateView.as_view(), name = "add_post"),
    path("post/<int:pk>/", PostDetailView.as_view(), name = "post_detail"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name = "post_update"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name = "post_delete"),
]
