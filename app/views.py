from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Post
# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
  posts = Post.objects.all()
  

  context = {
    'posts': posts,
    'posts_count': posts.count(),
  }

  if request.user.is_authenticated:
    context.update({'user_posts_count': posts.filter(poster=request.user).count()})

  return render(request, 'index.html', context=context)


class PostCreate(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['title', 'body']
  success_url = reverse_lazy('index')

  def form_valid(self, form):
    form.instance.poster = self.request.user
    return super().form_valid(form)