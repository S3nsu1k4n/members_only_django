from django.core.management.base import BaseCommand
from ...models import Post


class Command(BaseCommand):
    help = 'seed database for development'

    def handle(self, *args, **options):
        # execute seed command
        self.stdout.write('seeding data...')
        self.delete_all()
        self.seed()
        self.stdout.write('done')
        self.stdout.write(f'Created {Post.objects.all().count()} posts')

    def delete_all(self):
        """delete all posts in database"""
        Post.objects.all().delete()

    def seed(self):
        """Seeds the database"""
        # define some posts

        for post in [[f'Some title{i}', f'Some content{i}'] for i in range(10)]:
            Post.objects.create(title=post[0], body=post[1])
