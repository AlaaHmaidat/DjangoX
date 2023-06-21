from django.shortcuts import render

# Create your views here.

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Blog


class BlogListView(ListView):
    template_name = "blog/blog-list.html"
    model = Blog


class BlogDetailView(DetailView):
    template_name = "blog/blog-detail.html"
    model = Blog


class BlogCreateView(CreateView):
    template_name = "blog/blog-create.html"
    model = Blog
    fields = []


class BlogUpdateView(UpdateView):
    template_name = "blog/blog-update.html"
    model = Blog
    fields = []


class BlogDeleteView(DeleteView):
    template_name = "blog/blog-delete.html"
    model = Blog
    success_url = reverse_lazy("blog_list")