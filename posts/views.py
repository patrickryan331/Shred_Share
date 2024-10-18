from django.views.generic import TemplateView, ListView, DetailView
from .models import Post
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = (
            Post.objects.order_by("date").reverse()
        )


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/details.html'
