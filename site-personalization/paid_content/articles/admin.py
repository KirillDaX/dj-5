from django.contrib import admin
from articles.models import Article, User


class ArticleAdmin(admin.ModelAdmin):
    pass


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
admin.site.register(User, UserAdmin)
