from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'body', 'poster', 'created_at', 'updated_at')
  list_filter = ('poster', 'created_at', 'updated_at')