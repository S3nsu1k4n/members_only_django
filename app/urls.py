from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/create/', views.PostCreate.as_view(), name='post-create')
]