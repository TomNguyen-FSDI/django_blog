from django.urls import path
from .views import BlogListView
from .views import BlogDetailView
from .views import (
    BlogCreateView, BlogUpdateView, BlogDeleteView, 
    BlogAboutView
    )
#pk - primary key

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", BlogDetailView.as_view(),  name="post_detail"),
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path("post/aboutme/", BlogAboutView.as_view(), name="aboutme")
]