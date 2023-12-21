from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
  """Representing a Post created by a user
  
  Parameters
  ----------
  title : CharField
  body : TextField
  poster : ForeignKey(User)
  created_at : DateTimeField
  updated_at : DateTimeField
  """
  title = models.CharField(max_length=100, help_text='Title of the post')
  body = models.TextField(max_length=1000, help_text='Body of the post')
  poster = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, help_text='Who posted it')

  created_at = models.DateTimeField(auto_now_add=True, help_text='When the post was created')
  updated_at = models.DateTimeField(auto_now=True, help_text='When this post was last updated')

  def __str__(self):
    return self.title + f' {self.id}'
  
  def get_absolute_url(self):
    return reverse('post-detail')