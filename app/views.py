from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
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


class PostCreate(CreateView):
  model = Post
  fields = ['title', 'body']
  success_url = reverse_lazy('index')

  def form_valid(self, form):
    form.instance.poster = self.request.user
    return super().form_valid(form)