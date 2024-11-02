from django.contrib import admin
from .models import BlogArticles

class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "author","publish") # The value of 'list_display' must be a list or tuple
    list_filter = ("publish","author")
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ['-publish', 'author']

admin.site.register(BlogArticles,BlogArticlesAdmin)
