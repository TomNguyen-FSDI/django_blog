from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView  # new 
from .models import Post
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView 
    )

class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    #context_object_name = "all_posts_list"  # by default it returns object_list to the template home.html


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ['title', 'author', 'body']
    

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")  # blocking call. wait until this is done deleting and than load the home page

class BlogAboutView(ListView):
    model = Post
    template_name = "about_me.html"