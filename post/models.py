from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django import forms
# убрал ненужные импорты


class Category(models.Model):
    short_name = models.CharField('Короткое название', max_length=50)
    # полное название заменим просто на name и у всех CharField надо указывать атрибут max_length
    name = models.CharField('Название', max_length=255)
    description = models.CharField('описание', max_length=45)

    # во-первых здесь должно быть name, а article
    # а во-вторых fk должен быть в модели Article на модель Category. у нас не у каждой категории есть статья, а у каждой статьи есть категория
    # поэтому я отсюда это комментирую и переношу в модель article

    # name = models.ForeignKey(Article)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField('название статьи', max_length=255)
    image = models.ImageField('прикрепленная картинка', blank=True, null=True, upload_to='article_images/')
    author = models.CharField('автор', max_length=40)
    # контент статьи куда подевал?)
    content = RichTextUploadingField('Контент', blank=True, default='')
    category = models.ForeignKey(Category, related_name='categores', verbose_name='категория')
    created = models.DateTimeField('дата добавления', auto_now_add=True)
    likes = models.IntegerField('лайки', default=0, editable=False) #editable - не будет отображаться в админке

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created']

    def __str__(self):
        return self.name

class Comments(models.Model):
    comments_text = models.CharField(verbose_name='комментарий', max_length=400)
    comments_aricle = models.ForeignKey(Article,related_name='article')
    comments_date = models.DateTimeField('дата добавления', auto_now_add=True)
    comments_user = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.comments_text




