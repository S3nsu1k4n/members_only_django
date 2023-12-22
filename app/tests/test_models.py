from django.test import TestCase
from app.models import Post
from django.contrib.auth import get_user_model
User = get_user_model()

class PostModelTest(TestCase):
  """Tests Post model"""

  @classmethod
  def setUpTestData(cls) -> None:
    Post.objects.create(title='Some title', body='Some contents')

  def test_title_label(self):
    post = Post.objects.get(id=1)
    field_label = post._meta.get_field('title').verbose_name
    self.assertEqual(field_label, 'title')

  def test_title_length(self):
    post = Post.objects.get(id=1)
    max_length = post._meta.get_field('title').max_length
    self.assertEqual(max_length, 100)

  def test_body_label(self):
    post = Post.objects.get(id=1)
    field_label = post._meta.get_field('body').verbose_name
    self.assertEqual(field_label, 'body')

  def test_body_length(self):
    post = Post.objects.get(id=1)
    max_length = post._meta.get_field('body').max_length
    self.assertEqual(max_length, 1000)