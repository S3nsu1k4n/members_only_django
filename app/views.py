from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post
# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
  posts = Post.objects.all()

  context = {
    'posts': posts,
    'posts_count': posts.count(),
  }
  return render(request, 'index.html', context=context)