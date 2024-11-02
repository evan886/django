from  blog_api.views import add_article,modify_article
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/',add_article),
    path('articles/<int:art_id>',modify_article)
]
