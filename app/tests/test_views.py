from django.test import TestCase
from app.models import Post
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()


class LoginTest(TestCase):
  
  def test_view_url_exists_at_desired_location(self) -> None:
    """Checks if the url of the view exists"""
    response = self.client.get('/accounts/login/')
    self.assertEqual(response.status_code, 200)

  def test_correct_template(self) -> None:
    """Checks if the correct template is used"""
    response = self.client.get('/accounts/login/')
    self.assertTemplateUsed(response, 'registration/login.html')


class IndexTest(TestCase):
  @classmethod
  def setUpTestData(cls) -> None:
    """Create user and save to database"""
    test_user = User.objects.create_user(username='testuser', password='1X<ISRUkw+tuK')
    test_user.save()

  def test_uses_correct_template(self):
    """Tests if user is logged in correctly and get the correct templates"""
    response = self.client.get(reverse('index'))

    # Check that we got a response "success"
    self.assertEqual(response.status_code, 200)

    # Check we used correct template
    self.assertTemplateUsed(response, 'index.html')
    self.assertTemplateUsed(response, 'base_generic.html')


class PostCreateTest(TestCase):
  @classmethod
  def setUpTestData(cls) -> None:
    """Create user and save to database"""
    test_user = User.objects.create_user(username='testuser', password='1X<ISRUkw+tuK')
    test_user2 = User.objects.create_user(username='testuser2', password='1X<ISRUkw+tuK')
    test_user.save()
    test_user2.save()

  def test_redirect_if_not_logged_in(self) -> None:
    """Tests if redirect is returned if user is not logged in"""
    response = self.client.get(reverse('post-create'))
    self.assertRedirects(response, '/accounts/login/?next=/app/post/create/')

  def test_logged_in_uses_correct_template(self) -> None:
    """Tests if user is logged in correctly and get the correct templates"""
    login = self.client.login(username='testuser', password='1X<ISRUkw+tuK')
    response = self.client.get(reverse('post-create'))

    # Check user is logged in
    self.assertEqual(str(response.context['user']), 'testuser')
    # Check that we got a response "success"
    self.assertEqual(response.status_code, 200)

    # Check we used correct template
    self.assertTemplateUsed(response, 'app/post_form.html')
    self.assertTemplateUsed(response, 'base_generic.html')

  def test_form_submission(self) -> None:
    """Tests if the form correctly adds a new fruit"""
    user = User.objects.get(id=1)
    user2 = User.objects.get(id=2)
    login = self.client.login(username='testuser', password='1X<ISRUkw+tuK')
    form_data = {
      'title': 'some title',
      'body': 'some content',
      'poster': user,
    }
    response = self.client.post(reverse('post-create'), data=form_data)
    # Check if the form submission is successful
    self.assertRedirects(response, reverse('index'))

    post = Post.objects.get(id=1)
    
    # check if create was succesful
    self.assertEqual(post.title, form_data['title'])
    self.assertEqual(post.body, form_data['body'])
    self.assertEqual(post.poster, user)
    self.assertNotEqual(post.poster, user2)