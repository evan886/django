from django.contrib import admin
from .models import BlogArticles

class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish")
    list_filter = ("publish", "author")
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ['-publish', 'author']

admin.site.register(BlogArticles, BlogArticlesAdmin)



 raw_id_fields = ("author",) 注意 ,后  list
ERRORS:
<class 'blog.admin.BlogArticlesAdmin'>: (admin.E001) The value of 'raw_id_fields' must be a list or tuple.
