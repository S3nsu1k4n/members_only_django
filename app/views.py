from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post
# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
  return render(request, 'index.html')