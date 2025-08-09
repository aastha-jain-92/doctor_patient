from django.contrib import admin
from .models import BlogPost
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "is_draft", "created_at")
    list_filter = ("is_draft", "category")
    search_fields = ("title", "summary", "content")
