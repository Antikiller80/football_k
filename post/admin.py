from django.contrib import admin
from .models import Article, Category, Comments
# Register your models here.


class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    inlines = [ArticleInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)

